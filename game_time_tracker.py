from concurrent.futures import ThreadPoolExecutor
from threading import Event
from time import sleep

from requests.exceptions import ConnectionError

from fake_lcu import FakeLCU
from lcu import LCU


class GameTimeTracker:
    def __init__(self, testing: bool = False):
        self._game_time: float = -999
        # self._game_timer_difference_observers = []
        self._game_time_observers = []
        self._in_game_observers = []
        self._ten_min_observers = []
        self._ten_min_flag = Event()
        self._in_game: bool = False
        self._out_of_game = Event()
        self._pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=1)
        self._future = None
        #! TESTING
        if testing:
            self._lcu = FakeLCU()
        else:
            self._lcu = LCU()
        #! END TESTING

    def add_game_time_observer_callback(self, observer):
        self._game_time_observers.append(observer)

    def add_in_game_observer_callback(self, observer):
        self._in_game_observers.append(observer)

    def add_ten_min_observer_callback(self, observer):
        self._ten_min_observers.append(observer)

    @property
    def game_time(self):
        return self._game_time

    @game_time.setter
    def game_time(self, value):
        self._game_time = value
        for observer in self._game_time_observers:
            observer(self.game_time)
        if self._ten_min_flag.is_set():
            return
        if int(self.game_time) >= 600:
            for observer in self._ten_min_observers:
                observer(self.game_time)
            self._ten_min_flag.set()

    @property
    def in_game(self):
        return self._in_game

    @in_game.setter
    def in_game(self, value):
        self._in_game = value
        if value:
            self._out_of_game.clear()
            self.sync_game_time()
            self.future = self._pool.submit(self.start_tracking)
        else:
            self._out_of_game.set()
            self.game_time = -999
            self._ten_min_flag.clear()
        for observer in self._in_game_observers:
            observer(value)

    def sync_game_time(self):
        try:
            game_stats = self._lcu.get_game_stats()
        except ConnectionError as err:
            print(err)
            print('Potentially not in game')
            self.in_game = False
        else:
            new_time = game_stats['gameTime']
            self.game_time = new_time

    def start_tracking(self):
        self._out_of_game.wait(1)
        while self.in_game:
            self.game_time = self.game_time + 1
            if int(self.game_time) % 60 == 0:
                self.sync_game_time()
            self._out_of_game.wait(1)
        return None

    def quit(self):
        self.in_game = False
        self._pool.shutdown(wait=True, cancel_futures=True)


if __name__ == '__main__':
    gtt = GameTimeTracker()
    # gtt.add_game_time_difference_observer_callback(print)
    gtt.add_in_game_observer_callback(print)
    gtt.game_time = 20
    gtt.in_game = True
