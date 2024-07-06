from concurrent.futures import ThreadPoolExecutor
from threading import Event

from requests.exceptions import ConnectionError

from fake_lcu import FakeLCU
from lcu import LCU


class GameTimeTracker:
    def __init__(self):
        self._game_time: float = -999
        self._game_timer_difference_observers = []
        self._in_game_observers = []
        self._in_game: bool = False
        self._out_of_game = Event()
        self._pool = ThreadPoolExecutor(max_workers=1)
        #! TESTING
        # lcu = LCU()
        self._lcu = FakeLCU()
        #! END TESTING

    def add_game_time_difference_observer_callback(self, observer):
        self._game_timer_difference_observers.append(observer)

    def add_in_game_observer_callback(self, observer):
        self._in_game_observers.append(observer)

    @property
    def game_time(self):
        return self._game_time

    @game_time.setter
    def game_time(self, value):
        self._game_time = value

    @property
    def in_game(self):
        return self._in_game

    @in_game.setter
    def in_game(self, value):
        self._in_game = value
        if value:
            self._out_of_game.clear()
            self.update_game_time(disable_sync=True)
            self._pool.submit(self.start_tracking)
        else:
            self._out_of_game.set()
            self.game_time = -999
        for observer in self._in_game_observers:
            observer(value)

    def update_game_time(self, disable_sync: bool = False):
        try:
            game_stats = self._lcu.get_game_stats()
        except ConnectionError as err:
            print(err)
            print('Potentially not in game')
            self.in_game = False
            # Do something
        else:
            new_time = game_stats['gameTime']
            if disable_sync:
                self.game_time = new_time
            else:
                self.sync_game_time(new_time)

    def start_tracking(self):
        while not self._out_of_game.is_set():
            if int(self.game_time) % 60 == 0:
                self.update_game_time()
            self._out_of_game.wait(1)
            self.game_time = self.game_time + 1

    def sync_game_time(self, new_time):
        difference = new_time - self.game_time
        if abs(difference) >= 2:
            self.game_time = new_time
            for observer in self._game_timer_difference_observers:
                observer(difference)


gtt = GameTimeTracker()
gtt.add_game_time_difference_observer_callback(print)
gtt.add_in_game_observer_callback(print)
gtt.game_time = 20
gtt.in_game = True
