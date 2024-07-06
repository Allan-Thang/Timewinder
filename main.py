import sys

from app import App
from cooldown_timer import CooldownTimer
from game_time_tracker import GameTimeTracker
from summoner_spell_tracker_v2 import SpellTracker

#! pyinstaller --name Timewinder --onefile --windowed --icon=icon.icon main.py


class Timewinder():
    def __init__(self) -> None:
        self.gtt = GameTimeTracker()
        self.spell_tracker: SpellTracker = SpellTracker(self.gtt)
        self.cooldown_timer: CooldownTimer = CooldownTimer(self.gtt)
        self.app: App = App()

    def main(self) -> None:
        self.refresh()
        self.app.bind_refresh(self.refresh)
        self.app.root.mainloop()
        sys.exit()

    def refresh(self):
        self.gtt.in_game = False
        self.spell_tracker.refresh()
        self.spell_tracker.main()
        for i, enemy in enumerate(self.spell_tracker.enemy_list):
            self.app.configure_row_widgets(
                self.app.row_widgets_container[i], enemy, self)
        self.cooldown_timer.new_game(self.spell_tracker.enemy_list)
        self.gtt.in_game = True

    def update_and_start_cooldown(self, enemy, spell_used, cooldown_text_widget):
        self.spell_tracker.calculate_enemy_summoner_cooldowns(enemy)
        self.cooldown_timer.start_cooldown(
            enemy, spell_used, cooldown_text_widget)


def main():
    Timewinder().main()


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
