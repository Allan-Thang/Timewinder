import asyncio
import copy
from os import getenv

from dotenv import load_dotenv
from riotwatcher import LolWatcher

from dict_types import EnemyData, SummonerSpellData
from fake_lcu import FakeLCU
from fake_pf_game import FakePFGame
from game_time_tracker import GameTimeTracker
from lcu import LCU
from pulsefire_client import PulsefireClient


class SpellTracker:
    """
    A class to track summoner spells cooldowns.
    """

    def fetch_data_dragon_relevant_data(self) -> tuple[tuple, dict]:
        lol_watcher = LolWatcher(self.riot_dev_key)
        dd_versions = lol_watcher.data_dragon.versions_for_region('oce')
        dd_rune_data: tuple = lol_watcher.data_dragon.runes_reforged(
            dd_versions['v'])  # type: ignore
        dd_summoner_spells_data: dict = lol_watcher.data_dragon.summoner_spells(
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

        for row, _ in enumerate(inspiration_slots):
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

    def get_static_summoner_haste_sources(self, fetched_enemy):
        summoner_haste_sources = {}

        if self.inspiration_id == fetched_enemy['runes']['primaryRuneTree']['id'] or self.inspiration_id == fetched_enemy['runes']['secondaryRuneTree']['id']:
            summoner_haste_sources['Inspiration'] = True
        else:
            summoner_haste_sources['Inspiration'] = False

        if self.game_mode == 'ARAM':
            summoner_haste_sources['ARAM'] = True
        else:
            summoner_haste_sources['ARAM'] = False

        return summoner_haste_sources

    def enemy_dynamic_summoner_haste_sources(self, enemy: EnemyData):
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

    def get_relevent_enemy_data(self, enemy) -> EnemyData:
        riot_id: str = str(enemy['riotId'])
        champion_name: str = str(enemy['championName'])
        level: int = int(enemy['level'])
        items: list[str] = []

        # TODO: Move to a thread
        champion_icon: bytes = bytes(b'')
        # champion_icon: bytes = self.pulsefire_client.fetch_champ_icon(
        #     champion_name)

        summoner_spells: list[SummonerSpellData] = []
        enemy_summoner_spells_copy = dict(
            copy.deepcopy(enemy['summonerSpells']))
        for _, summoner_spell in enemy_summoner_spells_copy.items():
            spell_name = str(summoner_spell['displayName'])
            if 'Teleport' in spell_name:
                spell_name: str = 'Teleport'
            if 'Smite' in spell_name:
                spell_name: str = 'Smite'

            # summoner_spell['name'] = spell_name

            # TODO: Move to a thread
            summoner_spell_icon = b''
            # summoner_spell_icon = self.fetch_summoner_spell_icon(spell_name)

            summoner_spells.append(SummonerSpellData(name=spell_name,
                                                     base_cooldown=0,
                                                     starting_cooldown=0,
                                                     icon=summoner_spell_icon))

        summoner_haste_sources: dict = self.get_static_summoner_haste_sources(
            enemy)

        new_enemy = EnemyData(riot_id=riot_id,
                              champion_name=champion_name,
                              level=level,
                              items=items,
                              champion_icon=champion_icon,
                              summoner_spells=summoner_spells,
                              summoner_haste_sources=summoner_haste_sources,
                              summoner_haste=0)
        return new_enemy

    def fetch_summoner_spell_icon(self, summoner_spell_name: str) -> bytes:
        if summoner_spell_name in self.summoner_spell_icons:
            return self.summoner_spell_icons[summoner_spell_name]
        else:
            icon = self.pulsefire_client.fetch_summoner_spell_icon(
                summoner_spell_name)
            self.summoner_spell_icons[summoner_spell_name] = icon
            return icon

    def simplify_enemy_list(self, enemy_list: list[EnemyData]) -> list[EnemyData]:
        new_enemy_list = []
        for enemy in enemy_list:
            new_enemy_list.append(self.get_relevent_enemy_data(enemy))
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

    def check_for_cosmic_insight(self, enemy: EnemyData, active_game) -> bool:
        for participant in active_game['participants']:
            if enemy['riot_id'] not in participant['riotId']:
                continue
            if not enemy['summoner_haste_sources']['Inspiration']:
                return False
                # // enemy['summonerHasteSources']['Cosmic Insight'] = False
            if self.cosmic_insight_id not in participant['perks']['perkIds']:
                return False
                # // enemy['summonerHasteSources']['Cosmic Insight'] = False
            return True
            # // enemy['summonerHasteSources']['Cosmic Insight'] = True
        assert False, 'Unreachable code reached'

    def find_unique_summoner_spells(self) -> list[str]:
        summoner_list = []
        for enemy in self.enemy_list:
            for summoner_spell in enemy['summoner_spells']:
                if summoner_spell['name'] not in summoner_list:
                    summoner_list.append(summoner_spell['name'])
        return summoner_list

    def calculate_enemy_summoner_haste(self, enemy: EnemyData):
        summoner_haste = 0
        for source, haste in self.summoner_haste_sources.items():
            if enemy['summoner_haste_sources'][source]:
                summoner_haste += haste
        enemy['summoner_haste'] = summoner_haste

    def create_summoner_cooldown_dict(self, unique_summoner_spells: list[str], dd_summoner_spells_data: dict) -> dict[str, int]:
        summoner_cooldown_dict = {}
        for summoner_spell_name in unique_summoner_spells:
            for _, value in dd_summoner_spells_data['data'].items():
                if value['name'] in summoner_spell_name and self.game_mode in value['modes']:
                    summoner_cooldown_dict[summoner_spell_name] = value['cooldown'][0]
                    break
        return summoner_cooldown_dict

    def update_all_enemies_summoner_spell_base_cooldown(self, summoner_cd_dict: dict[str, int]):
        for enemy in self.enemy_list:
            self.update_enemy_summoner_spell_base_cooldown(
                enemy, summoner_cd_dict)

    def update_enemy_summoner_spell_base_cooldown(self, enemy: EnemyData, summoner_cd_dict: dict[str, int]):
        for enemy_summoner_spell in enemy['summoner_spells']:
            for summoner_spell, cooldown in summoner_cd_dict.items():
                if enemy_summoner_spell['name'] not in summoner_spell:
                    continue
                enemy_summoner_spell['base_cooldown'] = cooldown
                break
        return None

    def update_enemy_summoner_spell_starting_cooldown(self, enemy: EnemyData):
        for summoner_spell in enemy['summoner_spells']:
            base_cooldown = summoner_spell['base_cooldown']
            if 'Teleport' in summoner_spell['name']:
                base_cooldown = self.enemy_teleport_base_cooldown(
                    enemy, base_cooldown)
            summoner_spell['starting_cooldown'] = self.starting_cooldown(
                base_cooldown, enemy['summoner_haste'])

    def enemy_teleport_base_cooldown(self, enemy: EnemyData, base_cooldown: float) -> float:
        if (self.gtt.game_time) >= 600:
            return base_cooldown - (10 * min(enemy['level'], 10))
        return base_cooldown

    def starting_cooldown(self, base_cooldown: float, haste: int) -> float:
        return base_cooldown * (100/(100 + haste))

    def find_matching_enemy(self, champion_name):
        for enemy in self.enemy_list:
            if enemy['champion_name'] in champion_name:
                return enemy

    def calculate_all_enemy_summoner_cooldowns(self):
        for enemy in self.enemy_list:
            self.calculate_enemy_summoner_cooldowns(enemy)

    def calculate_enemy_summoner_cooldowns(self, enemy: EnemyData):
        self.update_enemy_items(enemy)
        dynamic_haste_sources = self.enemy_dynamic_summoner_haste_sources(
            enemy)
        # Merge with existing dict
        enemy['summoner_haste_sources'] |= dynamic_haste_sources
        self.calculate_enemy_summoner_haste(enemy)
        self.update_enemy_summoner_spell_starting_cooldown(enemy)

    def update_enemy_items(self, enemy: EnemyData):
        enemy_items_data = self.lcu.get_target_player_items(
            enemy['riot_id'])
        enemy_items = []
        for item in enemy_items_data:
            enemy_items.append(item['displayName'])
        enemy['items'] = enemy_items

    def __init__(self, gtt: GameTimeTracker, pulsefire_client: PulsefireClient, testing: bool = False):
        load_dotenv()
        self.gtt = gtt
        self.testing = testing
        self.riot_dev_key: str = str(getenv('RIOT_DEV_API_KEY'))
        self.my_summoner_name = getenv('SUMMONER_NAME')
        self.my_tag_line = getenv('GAME_TAG')
        self.riot_id = f'{self.my_summoner_name}#{self.my_tag_line}'
        self.summoner_haste_sources = {
            "Ionian Boots of Lucidity": 10,
            "Dawncore": 0,
            "Cosmic Insight": 18,
            "ARAM": 70,
        }
        self.pulsefire_client = pulsefire_client
        #! TESTING
        if testing:
            self.alt_lcu = False
            self.lcu = FakeLCU(self.alt_lcu)
        else:
            self.lcu = LCU()
        #! END TESTING
        self.summoner_spell_icons = {}
        self.game_mode = ''
        self.enemy_list: list[EnemyData] = []

        self.rune_data, self.summoner_spell_data = self.fetch_data_dragon_relevant_data()

        self.inspiration_id = self.parse_runeIDs_for_inspiration_ID(
            self.rune_data)
        self.cosmic_insight_id = self.parse_runeIDs_for_CI_ID(self.rune_data)
        #! TESTING
        if not testing:
            self.summoner = asyncio.run(self.pulsefire_client.fetch_summoner())
        #! END TESTING

    def main(self):
        #! TESTING
        if self.testing:
            active_game = FakePFGame().game
            self.lcu = FakeLCU(self.alt_lcu)
        else:
            active_game = asyncio.run(
                self.pulsefire_client.fetch_active_game(self.summoner))
        #! END TESTING

        player_list = self.get_player_list()
        self.game_mode = self.get_game_mode()
        my_team = self.get_my_team(self.riot_id, player_list)

        fetched_enemy_list = self.new_enemy_list(my_team, player_list)
        self.enemy_list = self.simplify_enemy_list(fetched_enemy_list)

        # // enemies_with_inspiration = self.get_enemies_with_inspiration(self.enemy_list)
        # // enemies_with_Cosmic_Insight_checklist = self.check_for_Cosmic_Insight(enemies_with_inspiration, active_game)
        # // self.update_enemies_with_cosmic_insight(enemies_with_inspiration, enemies_with_Cosmic_Insight_checklist)

        for enemy in self.enemy_list:
            enemy['summoner_haste_sources']['Cosmic Insight'] = self.check_for_cosmic_insight(
                enemy, active_game)

        unique_summoner_spells = self.find_unique_summoner_spells()
        summoner_cd_dict = self.create_summoner_cooldown_dict(
            unique_summoner_spells, self.summoner_spell_data)

        self.update_all_enemies_summoner_spell_base_cooldown(summoner_cd_dict)

        if self.testing:
            self.alt_lcu = True

        # self.calculate_all_enemies_summoner_cooldowns()

    def refresh(self):
        self.game_mode = ''
        self.enemy_list = []


def main():
    spell_tracker = SpellTracker(GameTimeTracker(), PulsefireClient())
    spell_tracker.main()
    for enemy in spell_tracker.enemy_list:
        spell_tracker.calculate_enemy_summoner_cooldowns(enemy)


# ? API_Key_Link = 'https://developer.riotgames.com'
if __name__ == '__main__':
    main()
