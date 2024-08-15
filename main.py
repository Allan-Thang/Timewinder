import sys
from concurrent.futures import ThreadPoolExecutor

from app import App
from cooldown_timer import CooldownTimer
from dict_types import EnemyData, SummonerSpellData
from game_time_tracker import GameTimeTracker
from pulsefire_client import PulsefireClient
from summoner_spell_tracker_v2 import SpellTracker

#! pyinstaller --name Timewinder --onefile --windowed --icon=icon.icon main.py

# TODO: Add right click event to shorten cooldown, Consider cacheing icons for faster startup, Consider adding regular spell tracking


class Timewinder():
    def __init__(self) -> None:
        self.testing = True
        self.gtt = GameTimeTracker(self.testing)
        self.pulsefire_client = PulsefireClient()
        self.spell_tracker: SpellTracker = SpellTracker(
            self.gtt, self.pulsefire_client, self.testing)
        self.cooldown_timer: CooldownTimer = CooldownTimer(self.gtt)
        self.app: App = App(self.gtt)
        self.champion_icons: dict[str, bytes] = {}
        self.summoner_spell_icons: dict[str, bytes] = {}

    def main(self) -> None:
        self.refresh()
        # self.app.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.app.bind_refresh(self.refresh)
        self.gtt.add_ten_min_observer_callback(self._ten_minute_callback)
        self.app.root.mainloop()
        # self.quit()

    def refresh(self):
        self.gtt.in_game = True
        self.spell_tracker.refresh()
        self.spell_tracker.main()
        self.fetch_icons(self.spell_tracker.enemy_list)
        for i, enemy in enumerate(self.spell_tracker.enemy_list):
            self.app.configure_row_widgets(
                self.app.row_widgets_container[i], enemy, self)
        self.app.root.after(1000, self.app.update_icons)
        self.cooldown_timer.new_game(
            self.spell_tracker.enemy_list, self.app.row_widgets_container)
        self.gtt.in_game = True

    def update_and_start_cooldown(self, enemy: EnemyData, spell_used: str):
        if not self.gtt.in_game:
            return
        self.spell_tracker.calculate_enemy_summoner_cooldowns(enemy)
        # self.cooldown_timer.start_cooldown(
        #     enemy, spell_used, cooldown_text_widget)
        self.cooldown_timer.trigger_cooldown(
            enemy, spell_used)

    def _ten_minute_callback(self):
        self.spell_tracker.calculate_all_enemy_summoner_cooldowns()
        self.cooldown_timer.update_teleport_starting_cooldown(
            self.spell_tracker.enemy_list)

    def quit(self):
        self.gtt.quit()
        # self.cooldown_timer.quit()
        # sleep(1)
        # self.app.root.quit()
        sys.exit()

    def fetch_icons(self, enemy_list: list[EnemyData]):
        pool = ThreadPoolExecutor()
        for enemy in enemy_list:
            pool.submit(self.fetch_champion_icon, enemy)

            for summoner_spell in enemy['summoner_spells']:
                pool.submit(self.fetch_summoner_spell_icon, summoner_spell)
        pool.shutdown(wait=False, cancel_futures=False)
        return None

    def fetch_champion_icon(self, enemy: EnemyData) -> None:
        champion_name = enemy['champion_name']
        if champion_name in self.champion_icons:
            enemy['champion_icon'] = self.champion_icons[champion_name]
            return None
        icon = self.pulsefire_client.fetch_champ_icon(champion_name)
        self.champion_icons[champion_name] = icon
        enemy['champion_icon'] = icon
        return None

    def fetch_summoner_spell_icon(self, summoner_spell: SummonerSpellData) -> None:
        summoner_spell_name = summoner_spell['name']
        if summoner_spell_name in self.summoner_spell_icons:
            summoner_spell['icon'] = self.summoner_spell_icons[summoner_spell_name]
            return None
        icon = self.pulsefire_client.fetch_summoner_spell_icon(
            summoner_spell_name)
        self.summoner_spell_icons[summoner_spell_name] = icon
        summoner_spell['icon'] = icon
        return None


def main():
    Timewinder().main()


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
