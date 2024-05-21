from app import App
from cooldown_timer import CooldownTimer
from summoner_spell_tracker_v2 import SpellTracker


class Main():
    def __init__(self) -> None:
        self.spell_tracker: SpellTracker = SpellTracker()
        self.cooldown_timer: CooldownTimer = CooldownTimer()
        self.app: App = App()

    def main(self) -> None:
        self.spell_tracker.main()
        for i, enemy in enumerate(self.spell_tracker.enemy_list):
            self.app.configure_row(
                self.app.row_widgets[i], enemy, self)
        self.app.root.mainloop()

    def update_and_start_cooldown(self, enemy, spell_used, cooldown_text_widget):
        self.spell_tracker.update_game_time()
        self.cooldown_timer.start_cooldown(
            enemy, spell_used, cooldown_text_widget, self.spell_tracker.game_time)


def main():
    Main().main()


if __name__ == '__main__':
    main()
