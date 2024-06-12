import threading
from time import sleep

from dict_types import Cooldown


class CooldownTimer:
    def __init__(self):
        # ? E.g. 'ZoeFlash': {cooldown: 100, thread: thread}
        # self._summoner_spell_cooldowns = {}
        self._cooldowns: list[Cooldown] = []
        self._game_time: int = 0
        self.in_game = False

    def set_game_time(self, game_time: int):
        self._game_time = game_time

    def start_game_timer(self):
        game_time = self._game_time
        while self.in_game:
            sleep(1)
            game_time = game_time + 1

    def check_in_game(self):
        self.in_game = True

    def track_summoner_spell_cooldown(self, enemy, summoner_spell_name: str, widget, active_summoner_spell):
        for key, summoner_spell in enemy['summonerSpells'].items():
            if summoner_spell_name in summoner_spell['name']:
                active_summoner_spell['thread'] = threading.current_thread()
                # self.countdown(summoner_spell['startingCooldown'])
                current_cooldown = summoner_spell['startingCooldown']
                # summoner_spell['currentCooldown'] = current_cooldown
                self.update_cooldown(
                    current_cooldown, active_summoner_spell, widget)
                while current_cooldown > 0 and active_summoner_spell['thread'] is threading.current_thread():
                    sleep(1)
                    current_cooldown = current_cooldown - 1
                    if 'Teleport' in summoner_spell_name:
                        current_cooldown = self.checked_teleport_cooldown(
                            summoner_spell, current_cooldown)
                    # summoner_spell['currentCooldown'] = current_cooldown
                    # enemy['summonerSpells'][key] = summoner_spell
                    self.update_cooldown(
                        current_cooldown, active_summoner_spell, widget)

                active_summoner_spell['thread'] = None
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
            widget.configure(text='Ready')
        else:
            widget.configure(text=str(current_cooldown))

    def new_cooldowns(self, enemy_list):
        for enemy in enemy_list:
            for _, summoner_spell in enemy['summonerSpells'].items():
                # self._summoner_spell_cooldowns[f'{enemy['championName']}{
                #     summoner_spell['name']}'] = {}
                # self._summoner_spell_cooldowns[f'{enemy["championName"]}{
                #     summoner_spell["name"]}']['cooldown'] = 0
                # self._summoner_spell_cooldowns[f'{enemy["championName"]}{
                #     summoner_spell["name"]}']['thread'] = None
                self._cooldowns.append(Cooldown({'name': f'{enemy["championName"]}{summoner_spell["name"]}', 'cooldown': 0, 'thread': None}))  # nopep8

    def find_cooldown(self, enemy_name: str, summoner_spell_name: str) -> Cooldown:
        for cooldown in self._cooldowns:
            if f'{enemy_name}{summoner_spell_name}' in cooldown['name']:
                return cooldown
        assert False

    def start_cooldown(self, enemy, summoner_spell_name: str, widget, game_time: int):
        # TODO: Find a way to detect if the game is over/new game
        # ? Use pulsefire_client.find_active_game > lcu.get_game_stats()
        if game_time < self._game_time:
            assert False
        # active_summoner_spell = self._summoner_spell_cooldowns[f'{
        #     enemy["championName"]}{summoner_spell_name}']
        active_summoner_spell = self.find_cooldown(
            f'{enemy['championName']}', f'{summoner_spell_name}')
        if active_summoner_spell['thread'] is None:
            thread = threading.Thread(
                target=self.track_summoner_spell_cooldown, args=(enemy, summoner_spell_name, widget, active_summoner_spell,))
            self.set_game_time(game_time)
            thread.daemon = True
            thread.start()
        else:
            # TODO: Reset cooldown
            active_summoner_spell['cooldown'] = 0
            active_summoner_spell['thread'] = None

            return
