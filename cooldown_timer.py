import concurrent.futures
from threading import Event

from dict_types import CooldownData, EnemyData, RowWidgets, SummonerSpellData
from game_time_tracker import GameTimeTracker


class CooldownTimer:
    def __init__(self, gtt: GameTimeTracker):
        self.gtt = gtt
        self.cooldowns: list[CooldownData] = []
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.stop_cooldowns = Event()
        # ? Immediately take off this amount when starting a cooldown
        self.rush = 5
        self.gtt.add_game_time_observer_callback(self._game_time_callback)
        self.gtt.add_in_game_observer_callback(self._in_game_callback)
        # How much to advance on right click
        self.advance_step = 1
        # How much to advance on middle click
        self.large_advance_step = 10

    def _game_time_callback(self, game_time: float):
        if self.stop_cooldowns.is_set():
            return None
        self.update_cooldowns()

    def _in_game_callback(self, in_game: bool):
        if in_game:
            self.stop_cooldowns.clear()
        if not in_game:
            self.stop_cooldowns.set()

    def update_teleport_starting_cooldown(self, enemy_list: list[EnemyData]) -> None:
        # At 10 minutes, Teleport upgrades to Unleashed Teleport and reduces the cooldown to its new max, including haste
        # Find all 'Teleport' cooldowns, update their starting cooldown and update current cooldown
        for cooldown in self.cooldowns:
            if not cooldown['on_cooldown']:
                continue
            if 'Teleport' not in cooldown['spell_name']:
                continue
            for enemy in enemy_list:
                # Find the corresponding enemy
                if not enemy['champion_name'] in cooldown['champion_name']:
                    continue
                # Get their Teleport spell if it exists
                teleport = self.find_enemy_summoner_spell(
                    enemy, 'Teleport')
                # If it doesn't exist, break and move to the next enemy
                if not teleport:
                    break
                cooldown['starting_cooldown'] = teleport['starting_cooldown']
                # Use the lower of the 2 cooldowns
                new_cooldown = cooldown['starting_cooldown']
                old_cooldown = cooldown['remaining_time']
                if new_cooldown < old_cooldown:
                    # Behave as if the new cooldown was created and triggered
                    cooldown['remaining_time'] = new_cooldown
                    cooldown['start_time'] = self.gtt.game_time
        self.update_cooldowns()
        return None

    def new_cooldowns(self, enemy_list: list[EnemyData], row_widgets_container) -> None:
        cooldowns = []
        for enemy in enemy_list:
            for summoner_spell in enemy['summoner_spells']:
                widget = self.find_widget(
                    enemy['champion_name'], summoner_spell['name'], row_widgets_container)
                cooldowns.append(CooldownData({'champion_name': enemy['champion_name'], 'spell_name': summoner_spell['name'], 'on_cooldown': False, 'start_time': 0, 'starting_cooldown': 0, 'remaining_time': 0, 'widget': widget}))  # nopep8
        self.cooldowns = cooldowns
        return None

    def find_cooldown(self, enemy_name: str, summoner_spell_name: str) -> CooldownData:
        for cooldown in self.cooldowns:
            if enemy_name in cooldown['champion_name'] and summoner_spell_name in cooldown['spell_name']:
                return cooldown
        assert False, f'{enemy_name}{summoner_spell_name} not found in cooldowns!'  # nopep8

    def find_enemy_summoner_spell(self, enemy: EnemyData, summoner_spell_name: str) -> dict | SummonerSpellData:
        for summoner_spell in enemy['summoner_spells']:
            if summoner_spell_name in summoner_spell['name']:
                return dict(summoner_spell)
        return {}

    def find_widget(self, enemy_name: str, summoner_spell_name: str, row_widgets_container: list[RowWidgets]) -> object:
        for row_widget in row_widgets_container:
            if enemy_name in row_widget['champion_name']:
                if summoner_spell_name in row_widget['summoner_spell_one_image'].cget('text'):
                    return row_widget['summoner_spell_one_cooldown']
                if summoner_spell_name in row_widget['summoner_spell_two_image'].cget('text'):
                    return row_widget['summoner_spell_two_cooldown']
        assert False, f'No matching widget found for {
            enemy_name}!{summoner_spell_name}!'

    def trigger_cooldown(self, enemy: EnemyData, summoner_spell_name: str):
        if not self.gtt.in_game:
            assert False, 'Not in game!'
        active_summoner_spell = self.find_cooldown(
            enemy['champion_name'], summoner_spell_name)
        # If on cooldown
        if active_summoner_spell['on_cooldown']:
            # Cancel cooldown
            self.reset_cooldown(active_summoner_spell)
        # If not on cooldown
        else:
            # Start cooldown
            self.start_cooldown(enemy, summoner_spell_name,
                                active_summoner_spell)
        self.update_cooldowns()
        return None

    def advance_cooldown(self, enemy: EnemyData, summoner_spell_name: str, large_advance=False) -> None:
        if not self.gtt.in_game:
            assert False, 'Not in game!'
        cooldown = self.find_cooldown(
            enemy['champion_name'], summoner_spell_name)
        if large_advance:
            cooldown['start_time'] -= self.large_advance_step
        else:
            cooldown['start_time'] -= self.advance_step
        self.update_cooldowns()

    def reset_cooldown(self, cooldown: CooldownData) -> None:
        cooldown['on_cooldown'] = False
        cooldown['start_time'] = 0
        cooldown['starting_cooldown'] = 0
        cooldown['remaining_time'] = 0

    def start_cooldown(self, enemy: EnemyData, summoner_spell_name: str, active_summoner_spell: CooldownData) -> None:
        enemy_summoner_spell = self.find_enemy_summoner_spell(
            enemy, summoner_spell_name)
        if not enemy_summoner_spell:
            assert False, 'Could not find enemy summoner spell!'
        active_summoner_spell['on_cooldown'] = True
        active_summoner_spell['start_time'] = self.gtt.game_time
        active_summoner_spell['starting_cooldown'] = enemy_summoner_spell['starting_cooldown'] - self.rush
        return None

    def track_cooldowns(self) -> None:
        while (self.gtt.in_game and not self.stop_cooldowns.is_set()):
            self.update_cooldowns()
            self.stop_cooldowns.wait(1)
        return None

    def update_cooldowns(self) -> None:
        for cooldown in self.cooldowns:
            if cooldown['on_cooldown']:
                cooldown['remaining_time'] = cooldown['starting_cooldown'] - \
                    self.gtt.game_time + cooldown['start_time']
                if cooldown['remaining_time'] > cooldown['starting_cooldown']:
                    print(f'{cooldown['champion_name']}!{cooldown['spell_name']}\'s remaining time of {cooldown["remaining_time"]} is more than starting cooldown, setting remaining time to starting cooldown {cooldown["starting_cooldown"]}')  # nopep8
                    cooldown['remaining_time'] = cooldown['starting_cooldown']
                    cooldown['start_time'] = self.gtt.game_time
                if cooldown['remaining_time'] <= 0:
                    self.reset_cooldown(cooldown)
            self.update_widget(cooldown)
        return None

    def update_widget(self, cooldown: CooldownData) -> None:
        if cooldown['on_cooldown']:
            cooldown['widget'].configure(
                text=str(int(cooldown['remaining_time'])))
            if 'red' not in str(cooldown['widget'].cget('foreground')):
                cooldown['widget'].configure(foreground='red')
        else:
            cooldown['widget'].configure(text='Ready', foreground='green')

    def new_game(self, enemy_list: list[EnemyData], row_widgets_container: list) -> None:
        self.new_cooldowns(enemy_list, row_widgets_container)
        self.update_cooldowns()

    def quit(self):
        self.cancel_all_cooldown_timers()

    def cancel_all_cooldown_timers(self):
        for cooldown in self.cooldowns:
            self.reset_cooldown(cooldown)
