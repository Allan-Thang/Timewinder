import concurrent.futures
import threading
from time import sleep

from requests.exceptions import ConnectionError

from dict_types import Cooldown
from fake_lcu import FakeLCU
from lcu import LCU


class CooldownTimer:
    def __init__(self):
        # ? E.g. 'ZoeFlash': {cooldown: 100, thread: thread}
        # self._summoner_spell_cooldowns = {}
        self._cooldowns: list[Cooldown] = []
        self._game_time: int = 0
        self.in_game = False
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=12)

    def set_game_time(self, game_time: int):
        self._game_time = game_time

    def start_game_timer(self, starting_game_time: int):
        self.pool.submit(self._start_game_timer, starting_game_time)

    def _start_game_timer(self, starting_game_time: int):
        self._game_time = starting_game_time
        while self.in_game:
            sleep(1)
            self._game_time += 1
            if self._game_time % 60 == 0:
                self.pool.submit(self.sync_with_game)

    def sync_with_game(self):
        #! TESTING
        # lcu = LCU()
        lcu = FakeLCU()
        #! END TESTING
        try:
            game_stats = lcu.get_game_stats()
        except ConnectionError as err:
            print(err)
            print('Potentially not in game')
            self.in_game = False
            return None
        else:
            self.in_game = True
            self._game_time = game_stats['gameTime']
            return None

    def track_summoner_spell_cooldown(self, enemy, summoner_spell_name: str, widget, active_summoner_spell: Cooldown):
        for key, summoner_spell in enemy['summonerSpells'].items():
            if summoner_spell_name in summoner_spell['name']:
                active_summoner_spell['thread'] = threading.current_thread()
                # self.countdown(summoner_spell['startingCooldown'])
                current_cooldown = summoner_spell['startingCooldown']
                # summoner_spell['currentCooldown'] = current_cooldown
                # self.update_cooldown(
                #     current_cooldown, active_summoner_spell, widget)
                while current_cooldown > 0 and active_summoner_spell['thread'] is threading.current_thread() and not active_summoner_spell['stop'].is_set():
                    # summoner_spell['currentCooldown'] = current_cooldown
                    # enemy['summonerSpells'][key] = summoner_spell
                    self.update_cooldown(
                        current_cooldown, active_summoner_spell, widget)
                    active_summoner_spell['stop'].wait(1)
                    current_cooldown = current_cooldown - 1
                    if 'Teleport' in summoner_spell_name:
                        current_cooldown = self.checked_teleport_cooldown(
                            summoner_spell, current_cooldown)
                self.update_cooldown(0, active_summoner_spell, widget)
                active_summoner_spell['thread'] = None
                active_summoner_spell['stop'].clear()
                print(f'{enemy['championName']}\'s {summoner_spell["name"]} is ready!')  # nopep8
                return
        assert False

    def checked_teleport_cooldown(self, summoner_spell, current_cooldown: int) -> int:
        if self._game_time < 600:
            return current_cooldown

        starting_cooldown: int = summoner_spell['startingCooldown']
        if current_cooldown > starting_cooldown:
            return starting_cooldown
        else:
            return current_cooldown

    def update_cooldown(self, current_cooldown, active_summoner_spell, widget):
        active_summoner_spell['cooldown'] = current_cooldown
        if current_cooldown == 0:
            widget.configure(text='Ready', foreground='green')
            return None
        else:
            widget.configure(text=str(current_cooldown))
            #! Magic print makes the program work
            print(widget.cget('foreground'))
            if 'red' not in widget.cget('foreground'):
                widget.configure(foreground='red')
            return None

    def new_cooldowns(self, enemy_list):
        for enemy in enemy_list:
            for _, summoner_spell in enemy['summonerSpells'].items():
                # self._summoner_spell_cooldowns[f'{enemy['championName']}{
                #     summoner_spell['name']}'] = {}
                # self._summoner_spell_cooldowns[f'{enemy["championName"]}{
                #     summoner_spell["name"]}']['cooldown'] = 0
                # self._summoner_spell_cooldowns[f'{enemy["championName"]}{
                #     summoner_spell["name"]}']['thread'] = None
                self._cooldowns.append(Cooldown({'name': f'{enemy["championName"]}{summoner_spell["name"]}', 'cooldown': 0, 'thread': None, 'stop': threading.Event()}))  # nopep8
        return None

    def find_cooldown(self, enemy_name: str, summoner_spell_name: str) -> Cooldown:
        for cooldown in self._cooldowns:
            if f'{enemy_name}{summoner_spell_name}' in cooldown['name']:
                return cooldown
        assert False

    def start_cooldown(self, enemy, summoner_spell_name: str, widget):
        # TODO: Find a way to detect if the game is over/new game
        active_summoner_spell = self.find_cooldown(
            f'{enemy['championName']}', f'{summoner_spell_name}')
        if active_summoner_spell['thread'] is None:
            self.pool.submit(self.track_summoner_spell_cooldown,
                             enemy, summoner_spell_name, widget, active_summoner_spell)
            return None
        else:
            active_summoner_spell['stop'].set()
            return None
