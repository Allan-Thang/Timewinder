from os import getenv

from dotenv import load_dotenv
from riotwatcher import LolWatcher

from fake_lcu import FakeLCU
from fake_pf_game import FakePFGame
from lcu import LCU
# from pulsefire.clients import RiotAPIClient
from pulsefire_client import PulsefireClient


class SpellTracker:
    """
    A class to track summoner spells cooldowns.
    """

    def fetch_data_dragon_relevant_data(self):
        lol_watcher = LolWatcher(self.riot_dev_key)
        dd_versions = lol_watcher.data_dragon.versions_for_region('oce')
        dd_rune_data = lol_watcher.data_dragon.runes_reforged(
            dd_versions['v'])  # type: ignore
        dd_summoner_spells_data = lol_watcher.data_dragon.summoner_spells(
            dd_versions['v'])  # type: ignore
        return dd_rune_data, dd_summoner_spells_data

    def parse_runeIDs_for_inspiration_ID(self, dd_rune_ids):
        for rune_tree in dd_rune_ids:
            if 'Inspiration' in rune_tree['key']:
                return rune_tree['id']

    def parse_runeIDs_for_CI_ID(self, dd_rune_ids):

        CI_key = 'CosmicInsight'
        inspiration_tree_index = None

        for i, j in enumerate(dd_rune_ids):
            if 'Inspiration' in j['key']:
                inspiration_tree_index = i
                break

        # // for i in range(len(dd_rune_ids)):
        # //     if 'Inspiration' in dd_rune_ids[i]['key']:
        # //        inspiration_tree_index = i
        # //         break

        inspiration_slots = dd_rune_ids[inspiration_tree_index]['slots']

        for row, row_data in enumerate(inspiration_slots):
            for rune, rune_data in enumerate(inspiration_slots[row]['runes']):
                if CI_key in rune_data['key']:
                    return inspiration_slots[row]['runes'][rune]['id']

        # // for row in range(len(inspiration_slots)):
        # //     for rune in range(len(inspiration_slots[row]['runes'])):
        # //         if CI_key in inspiration_slots[row]['runes'][rune]['key']:
        # //             return inspiration_slots[row]['runes'][rune]['id']

    def get_player_list(self):
        player_list = self.lcu.get_all_players()
        return player_list

    def get_game_time(self) -> int:
        game_time = int(self.lcu.get_game_stats()['gameTime'])
        return game_time

    def update_game_time(self) -> None:
        self.game_time = self.get_game_time()
        return

    def set_game_time(self, game_time: int) -> None:
        self.game_time = game_time
        return

    def get_game_mode(self):
        game_mode = self.lcu.get_game_stats()['gameMode']
        return game_mode

    def get_my_team(self, riot_id, player_list):
        my_team = None
        for player in player_list:
            if player['riotId'] in riot_id:
                my_team = player['team']
                break
        return my_team

    def new_enemy_list(self, my_team, player_list):
        enemy_list = []
        for player in player_list:
            if my_team not in player['team']:
                enemy_list.append(player)
            if (len(enemy_list) >= 5):
                break
        return enemy_list

    def get_static_summoner_haste_sources(self, enemy):
        summoner_haste_sources = {}

        if self.inspiration_id == enemy['runes']['primaryRuneTree']['id'] or self.inspiration_id == enemy['runes']['secondaryRuneTree']['id']:
            summoner_haste_sources['Inspiration'] = True
        else:
            summoner_haste_sources['Inspiration'] = False

        if self.game_mode == 'ARAM':
            summoner_haste_sources['ARAM'] = True
        else:
            summoner_haste_sources['ARAM'] = False

        return summoner_haste_sources

    def enemy_dynamic_summoner_haste_sources(self, enemy):
        summoner_haste_sources = {}

        if 'Ionian Boots of Lucidity' in enemy['items']:
            summoner_haste_sources['Ionian Boots of Lucidity'] = True
        else:
            summoner_haste_sources['Ionian Boots of Lucidity'] = False

        if 'Dawncore' in enemy['items']:
            summoner_haste_sources['Dawncore'] = True
        else:
            summoner_haste_sources['Dawncore'] = False

        return summoner_haste_sources

    def get_relevent_enemy_data_dict(self, enemy):
        new_dict = {}
        new_dict['riotId'] = enemy['riotId']
        new_dict['championName'] = enemy['championName']
        new_dict['level'] = enemy['level']
        new_dict['items'] = []

        new_dict['summonerSpells'] = enemy['summonerSpells']
        for key, summoner_spell in new_dict['summonerSpells'].items():
            spell_name = str(summoner_spell['displayName'])
            if 'Teleport' in spell_name:
                spell_name = 'Teleport'

            summoner_spell = {}
            summoner_spell['name'] = spell_name

            summoner_spell['icon'] = self.fetch_summoner_spell_icon(spell_name)

            new_dict['summonerSpells'][key] = summoner_spell

        new_dict['summonerHasteSources'] = self.get_static_summoner_haste_sources(
            enemy)

        new_dict['championIcon'] = self.pulsefire_client.fetch_champ_icon(
            new_dict['championName'])
        return new_dict

    def fetch_summoner_spell_icon(self, summoner_spell_name: str) -> bytes:
        if summoner_spell_name in self.summoner_spell_icons:
            return self.summoner_spell_icons[summoner_spell_name]
        else:
            icon = self.pulsefire_client.fetch_summoner_spell_icon(
                summoner_spell_name)
            self.summoner_spell_icons[summoner_spell_name] = icon
            return icon

    def simplify_enemy_list(self, enemy_list):
        new_enemy_list = []
        for enemy in enemy_list:
            new_enemy_list.append(self.get_relevent_enemy_data_dict(enemy))
        return new_enemy_list

    # // def get_enemies_with_inspiration(self, enemy_list):
    # //     enemies_with_inspiration = []
    # //     for enemy in enemy_list:
    # //         if enemy['summonerHasteSources']['Inspiration']:
    # //             enemies_with_inspiration.append(enemy)
    # //     return enemies_with_inspiration

    # // def check_for_Cosmic_Insight(self, enemies_with_inspiration, active_game):
    # //     checklist = []
    # //     for enemy in enemies_with_inspiration:
    # //         for participant in active_game['participants']:
    # //             if participant['summonerName'] in enemy['summonerName']:
    # //                 if self.cosmic_insight_ID in participant['perks']['perkIDs']:
    # //                     checklist.append(True)
    # //                 else:
    # //                     checklist.append(False)
    # //     return checklist

    # // def update_enemies_with_cosmic_insight(self, enemies_with_inspiration, enemies_with_Cosmic_Insight_checklist):
    # //     for i in range(len(enemies_with_inspiration)):
    # //         enemies_with_inspiration[i]['summonerHasteSources']['Cosmic Insight'] = enemies_with_Cosmic_Insight_checklist[i]

    def check_for_cosmic_insight(self, enemy, active_game):
        for participant in active_game['participants']:
            if enemy['riotId'] not in participant['riotId']:
                continue
            if not enemy['summonerHasteSources']['Inspiration']:
                return False
                # // enemy['summonerHasteSources']['Cosmic Insight'] = False
            if self.cosmic_insight_id not in participant['perks']['perkIds']:
                return False
                # // enemy['summonerHasteSources']['Cosmic Insight'] = False
            return True
            # // enemy['summonerHasteSources']['Cosmic Insight'] = True

    def find_unique_summoner_spells(self, enemy_list):
        summoner_list = {}
        for enemy in enemy_list:
            for _, summoner_spell in enemy['summonerSpells'].items():
                if summoner_spell['name'] not in summoner_list:
                    summoner_list[summoner_spell['name']] = 0
        return summoner_list

    def calculate_enemy_summoner_haste(self, enemy):
        summoner_haste = 0
        for source in self.summoner_haste_sources:
            if enemy['summonerHasteSources'][source]:
                summoner_haste += self.summoner_haste_sources[source]
        enemy['summonerHaste'] = summoner_haste

    def create_summoner_cooldown_dict(self, unique_summoner_spells, dd_summoner_spells_data):
        summoner_cooldown_dict = {}
        for summoner_spell_name, _ in unique_summoner_spells.items():
            for _, value in dd_summoner_spells_data['data'].items():
                if value['name'] in summoner_spell_name and self.game_mode in value['modes']:
                    summoner_cooldown_dict[summoner_spell_name] = value['cooldown'][0]
                    break
        return summoner_cooldown_dict

    def update_all_enemies_summoner_spell_base_cooldown(self, enemy_list, summoner_cd_dict):
        for enemy in enemy_list:
            self.update_enemy_summoner_spell_base_cooldown(
                enemy, summoner_cd_dict)

    def update_enemy_summoner_spell_base_cooldown(self, enemy, summoner_cd_dict):
        for key, enemy_summoner_spell in enemy['summonerSpells'].items():
            for summoner_spell, cooldown in summoner_cd_dict.items():
                if enemy_summoner_spell['name'] in summoner_spell:
                    enemy_summoner_spell['baseCooldown'] = cooldown

                    enemy['summonerSpells'][key] = enemy_summoner_spell
                    break

    def update_enemy_summoner_spell_starting_cooldown(self, enemy):
        for key, summoner_spell in enemy['summonerSpells'].items():
            base_cooldown = summoner_spell['baseCooldown']
            if 'Teleport' in summoner_spell['name']:
                base_cooldown = self.enemy_teleport_base_cooldown(
                    enemy, base_cooldown)
            summoner_spell['startingCooldown'] = self.starting_cooldown(
                base_cooldown, enemy['summonerHaste'])
            enemy['summonerSpells'][key] = summoner_spell

    def enemy_teleport_base_cooldown(self, enemy, base_cooldown):
        if (self.game_time) >= 600:
            return base_cooldown - (10 * min(enemy['level'], 10))
        return base_cooldown

    def starting_cooldown(self, base_cooldown, haste):
        return int(base_cooldown * (100/(100 + haste)))

    def find_matching_enemy(self, champion_name):
        for enemy in self.enemy_list:
            if enemy['championName'] in champion_name:
                return enemy

    def calculate_enemy_summoner_cooldowns(self, enemy):
        self.update_enemy_items(enemy)
        dynamic_haste_sources = self.enemy_dynamic_summoner_haste_sources(
            enemy)
        # Merge with existing dict
        enemy['summonerHasteSources'] |= dynamic_haste_sources
        self.calculate_enemy_summoner_haste(enemy)
        self.update_enemy_summoner_spell_starting_cooldown(enemy)

    def update_enemy_items(self, enemy):
        enemy_items_data = self.lcu.get_target_player_items(
            enemy['riotId'])
        enemy_items = []
        for item in enemy_items_data:
            enemy_items.append(item['displayName'])
        enemy['items'] = enemy_items

    def __init__(self):
        load_dotenv()
        self.riot_dev_key: str = str(getenv('RIOT_DEV_API_KEY'))
        self.my_summoner_name = getenv('SUMMONER_NAME')
        self.my_tag_line = getenv('GAME_TAG')
        self.riot_id = f'{self.my_summoner_name}#{self.my_tag_line}'
        self.summoner_haste_sources = {
            "Ionian Boots of Lucidity": 12,
            "Dawncore": 0,
            "Cosmic Insight": 18,
            "ARAM": 70,
        }
        self.pulsefire_client = PulsefireClient(self.riot_dev_key)
        #! TESTING
        # self.lcu = LCU()
        self.lcu = FakeLCU()
        #! END TESTING
        self.summoner_spell_icons = {}
        self.game_time: int = 0
        self.game_mode = ''
        self.enemy_list = []

        self.rune_data, self.summoner_spell_data = self.fetch_data_dragon_relevant_data()

        self.inspiration_id = self.parse_runeIDs_for_inspiration_ID(
            self.rune_data)
        self.cosmic_insight_id = self.parse_runeIDs_for_CI_ID(self.rune_data)
        #! TESTING
        # self.summoner = asyncio.run(self.pulsefire_client.fetch_summoner())
        #! END TESTING

    def main(self):
        #! TESTING
        # active_game = asyncio.run(
        #     self.pulsefire_client.fetch_active_game(self.summoner))
        active_game = FakePFGame().game
        #! END TESTING

        player_list = self.get_player_list()
        self.update_game_time()
        self.game_mode = self.get_game_mode()
        my_team = self.get_my_team(self.riot_id, player_list)

        self.enemy_list = self.new_enemy_list(my_team, player_list)
        self.enemy_list = self.simplify_enemy_list(self.enemy_list)

        # // enemies_with_inspiration = self.get_enemies_with_inspiration(self.enemy_list)
        # // enemies_with_Cosmic_Insight_checklist = self.check_for_Cosmic_Insight(enemies_with_inspiration, active_game)
        # // self.update_enemies_with_cosmic_insight(enemies_with_inspiration, enemies_with_Cosmic_Insight_checklist)

        for enemy in self.enemy_list:
            enemy['summonerHasteSources']['Cosmic Insight'] = self.check_for_cosmic_insight(
                enemy, active_game)

        unique_summoner_spells = self.find_unique_summoner_spells(
            self.enemy_list)
        summoner_cd_dict = self.create_summoner_cooldown_dict(
            unique_summoner_spells, self.summoner_spell_data)

        self.update_all_enemies_summoner_spell_base_cooldown(
            self.enemy_list, summoner_cd_dict)

        # self.calculate_all_enemies_summoner_cooldowns()


def main():
    spell_tracker = SpellTracker()
    spell_tracker.main()
    for enemy in spell_tracker.enemy_list:
        spell_tracker.calculate_enemy_summoner_cooldowns(enemy)


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
