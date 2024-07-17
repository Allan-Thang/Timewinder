import sys
from time import sleep

from app import App
from cooldown_timer import CooldownTimer
from game_time_tracker import GameTimeTracker
from summoner_spell_tracker_v2 import SpellTracker

#! pyinstaller --name Timewinder --onefile --windowed --icon=icon.icon main.py

# TODO: Optimization of startup


class Timewinder():
    def __init__(self) -> None:
        self.testing = True
        self.gtt = GameTimeTracker(self.testing)
        self.spell_tracker: SpellTracker = SpellTracker(self.gtt, self.testing)
        self.cooldown_timer: CooldownTimer = CooldownTimer(self.gtt)
        self.app: App = App(self.gtt)

    def main(self) -> None:
        self.refresh()
        # self.app.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.app.bind_refresh(self.refresh)
        self.gtt.add_ten_min_observer_callback(self._ten_minute_callback)
        self.app.root.mainloop()
        # self.quit()

    def refresh(self):
        self.gtt.in_game = False
        self.spell_tracker.refresh()
        self.spell_tracker.main()
        for i, enemy in enumerate(self.spell_tracker.enemy_list):
            self.app.configure_row_widgets(
                self.app.row_widgets_container[i], enemy, self)
        self.cooldown_timer.new_game(
            self.spell_tracker.enemy_list, self.app.row_widgets_container)
        self.gtt.in_game = True

    def update_and_start_cooldown(self, enemy: dict, spell_used: str):
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
        sleep(1)
        # self.app.root.quit()
        sys.exit()


def main():
    Timewinder().main()


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
