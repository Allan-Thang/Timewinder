import concurrent.futures
from threading import Event, current_thread

from dict_types import Cooldown
from game_time_tracker import GameTimeTracker


class CooldownTimer:
    def __init__(self, gtt: GameTimeTracker):
        # ? E.g. 'ZoeFlash': {cooldown: 100, thread: thread}
        self.gtt = gtt
        self._cooldowns: list[Cooldown] = []
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=12)
        # ? Immediately take off this amount when starting a cooldown
        self.rush = 5
        self.gtt.add_in_game_observer_callback(self.in_game_callback)
        self.gtt.add_game_time_difference_observer_callback(
            self.advance_all_cooldowns)

    def cancel_all_cooldown_timers(self):
        if len(self._cooldowns) <= 0:
            return False
        for cooldown in self._cooldowns:
            cooldown['stop'].set()

    def in_game_callback(self, in_game: bool):
        if not in_game:
            self.cancel_all_cooldown_timers()

    def advance_all_cooldowns(self, advance_by: float):
        for cooldown in self._cooldowns:
            cooldown['cooldown'] -= int(advance_by)

    def track_summoner_spell_cooldown(self, enemy, summoner_spell_name: str, widget, active_summoner_spell: Cooldown):
        for _, summoner_spell in enemy['summonerSpells'].items():
            if summoner_spell_name in summoner_spell['name']:
                active_summoner_spell['thread'] = current_thread()
                active_summoner_spell['cooldown'] = summoner_spell['startingCooldown'] - self.rush
                while active_summoner_spell['cooldown'] > 0 and not active_summoner_spell['stop'].is_set():
                    self.update_cooldown(
                        active_summoner_spell['cooldown'], widget)
                    active_summoner_spell['stop'].wait(1)
                    active_summoner_spell['cooldown'] -= 1
                    if 'Teleport' in summoner_spell_name:
                        active_summoner_spell['cooldown'] = self.checked_teleport_cooldown(
                            summoner_spell, active_summoner_spell['cooldown'])
                self.update_cooldown(0, widget)
                active_summoner_spell['thread'] = None
                active_summoner_spell['stop'].clear()
                print(f'{enemy['championName']}\'s {summoner_spell["name"]} is ready!')  # nopep8
                return
        assert False

    def checked_teleport_cooldown(self, summoner_spell, current_cooldown: int) -> int:
        if self.gtt.game_time < 600:
            return current_cooldown

        starting_cooldown: int = summoner_spell['startingCooldown']
        if current_cooldown > starting_cooldown:
            return starting_cooldown
        else:
            return current_cooldown

    def update_cooldown(self, current_cooldown, widget):
        if current_cooldown <= 0:
            widget.configure(text='Ready', foreground='green')
            return None
        else:
            widget.configure(text=str(current_cooldown))
            if 'red' not in str(widget.cget('foreground')):
                widget.configure(foreground='red')
            return None

    def new_cooldowns(self, enemy_list):
        cooldowns = []
        for enemy in enemy_list:
            for _, summoner_spell in enemy['summonerSpells'].items():
                cooldowns.append(Cooldown({'name': f'{enemy["championName"]}{summoner_spell["name"]}', 'cooldown': 0, 'thread': None, 'stop': Event()}))  # nopep8
        self._cooldowns = cooldowns
        return None

    def find_cooldown(self, enemy_name: str, summoner_spell_name: str) -> Cooldown:
        for cooldown in self._cooldowns:
            if f'{enemy_name}{summoner_spell_name}' in cooldown['name']:
                return cooldown
        assert False

    def start_cooldown(self, enemy, summoner_spell_name: str, widget):
        if not self.gtt.in_game:
            assert False, 'Not in game!'
        active_summoner_spell = self.find_cooldown(
            f'{enemy['championName']}', f'{summoner_spell_name}')
        if active_summoner_spell['thread'] is not None:
            active_summoner_spell['stop'].set()
            return None
        self.pool.submit(self.track_summoner_spell_cooldown, enemy,
                         summoner_spell_name, widget, active_summoner_spell)
        return None

    def new_game(self, enemy_list):
        self.cancel_all_cooldown_timers()
        self.new_cooldowns(enemy_list)
