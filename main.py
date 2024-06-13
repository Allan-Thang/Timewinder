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
        self.cooldown_timer.in_game = True
        self.cooldown_timer.start_game_timer(self.spell_tracker.game_time)
        self.cooldown_timer.new_cooldowns(self.spell_tracker.enemy_list)
        for i, enemy in enumerate(self.spell_tracker.enemy_list):
            self.app.configure_row(
                self.app.row_widgets[i], enemy, self)
        self.app.root.mainloop()

    def update_and_start_cooldown(self, enemy, spell_used, cooldown_text_widget):
        # ? Before each cooldown: Items
        # * Get player items > calculate haste > start cooldown
        # ? Periodically: Game Time + still in game(If time errors, then not in game)
        # self.spell_tracker.update_game_time()
        self.spell_tracker.calculate_enemy_summoner_cooldowns(enemy)
        self.cooldown_timer.start_cooldown(
            enemy, spell_used, cooldown_text_widget)


def main():
    Main().main()


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
