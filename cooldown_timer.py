import threading
from time import sleep

class CooldownTimer:
    def __init__(self):
        self.active_cooldown_threads = []

    def get_active_cooldown_threads(self):
        return self.active_cooldown_threads

    def track_summoner_spell_cooldown(self, enemy, ssName: str):
        for key, summoner_spell in enemy['summonerSpells'].items():
            if ssName in summoner_spell['name']:
                # self.countdown(summoner_spell['startingCooldown'])
                summoner_spell['currentCooldown'] = summoner_spell['startingCooldown']
                while summoner_spell['currentCooldown'] > 0:
                    sleep(1)
                    summoner_spell['currentCooldown'] = summoner_spell['currentCooldown'] - 1
                    enemy['summonerSpells'][key] = summoner_spell

                print(f'{enemy['championName']}\'s {summoner_spell["name"]} is ready!')

    def start_cooldown(self, enemy, ssName: str):
        thread = threading.Thread(target = self.track_summoner_spell_cooldown, args=(enemy, ssName,))
        self.active_cooldown_threads.append(thread)
        thread.start()