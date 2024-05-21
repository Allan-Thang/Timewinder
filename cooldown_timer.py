import threading
from time import sleep


class CooldownTimer:
    def __init__(self):
        self._active_cooldown_threads = []
        self._game_time: int = 0

    def get_active_cooldown_threads(self):
        return self._active_cooldown_threads

    def set_game_time(self, game_time: int):
        self._game_time = game_time

    def track_summoner_spell_cooldown(self, enemy, summoner_spell_name: str, widget):
        for key, summoner_spell in enemy['summonerSpells'].items():
            if summoner_spell_name in summoner_spell['name']:
                # self.countdown(summoner_spell['startingCooldown'])
                current_cooldown = summoner_spell['startingCooldown']
                summoner_spell['currentCooldown'] = current_cooldown
                while current_cooldown > 0:
                    sleep(1)
                    current_cooldown = current_cooldown - 1
                    if 'Teleport' in summoner_spell_name:
                        current_cooldown = self.check_teleport_cooldown(
                            summoner_spell, current_cooldown)
                    summoner_spell['currentCooldown'] = current_cooldown
                    enemy['summonerSpells'][key] = summoner_spell
                    widget.configure(text=str(current_cooldown))
                    if current_cooldown == 0:
                        widget.configure(text='Ready')

                print(f'{enemy['championName']}\'s {
                      summoner_spell["name"]} is ready!')

    def check_teleport_cooldown(self, summoner_spell, current_cooldown: int) -> int:
        starting_cooldown: int = summoner_spell['startingCooldown']
        if self._game_time >= 600:
            if current_cooldown > starting_cooldown:
                return starting_cooldown
            else:
                return current_cooldown
        else:
            return current_cooldown

    def start_cooldown(self, enemy, summoner_spell_name: str, widget, game_time: int):
        """
        Starts a cooldown for a given summoner spell on an enemy character.

        Args:
            enemy (dict): A dictionary representing the enemy character with their summoner spells.
            summoner_spell_name (str): The name of the summoner spell to start the cooldown for.
            game_time (int): The current game time in seconds.

        Returns:
            None

        Raises:
            None

        Notes:
            - This function must be called after the cooldowns are calculated.
            - A new thread is created to track the summoner spell cooldown.
            - The game time is set using the provided `game_time` argument.
            - The newly created thread is appended to the `_active_cooldown_threads` list.
            - The thread is started.
        """
        thread = threading.Thread(
            target=self.track_summoner_spell_cooldown, args=(enemy, summoner_spell_name, widget,))
        self.set_game_time(game_time)
        self._active_cooldown_threads.append(thread)
        thread.start()
