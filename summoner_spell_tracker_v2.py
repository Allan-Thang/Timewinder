import requests
import aiohttp
import asyncio
import sys
from os import getenv
from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
from pulsefire.clients import RiotAPIClient

class LCU:
    def __init__(self):
        self.install_directory = None
        self.port = '2999'
        self.auth_key = None
        self.lcu_url = 'https://127.0.0.1'
        self.SSL_cert = 'C:\\Users\\Shiva\\Downloads\\riotgames.pem'

    # @staticmethod
    # def find_client_lockfile():
    #     c = wmi.WMI()
    #     for process in c.Win32_Process():
    #         if process.name == 'LeagueClientUx.exe':
    #             cmd = process.CommandLine
    #             for segment in cmd.split('" "'):
    #                 if '--app-port' in segment:
    #                     port = int(segment.split('=')[1])
    #                 if '--install-directory' in segment:
    #                     install_directory = segment.split('=')[1]
    #                 # break
            
    #     return install_directory, port
    
    # @staticmethod
    # def parse_locklife(install_directory):
    #     lockfile = os.path.join(install_directory, 'lockfile')
    #     with open(lockfile) as f:
    #         content = f.read()
    #     content = content.split(':')
    #     process, PID, port, password, protocol = content
    #     return process, PID, port, password, protocol

    # def load_auth_key(self):
    #     process, PID, port, password, protocol = self.parse_locklife(self.install_directory)
    #     auth_key = base64.b64encode(f'riot{password}'.encode()).decode()
    #     return auth_key

    # def load_start_data(self):
    #     self.install_directory, self.port = self.find_client_lockfile()
    #     self.auth_key = self.load_auth_key()
    #     return self.install_directory, self.port, self.auth_key

    # def load_start_data(self):
    #     self.port = '2999'

    def get_all_game_data(self):
        r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/allgamedata', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=False)
        return r
    
    def get_active_player_data(self):
        r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/activeplayer', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
        return r
    
    # def get_active_player_name(self):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/activeplayername', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
    #     return r
    
    # def get_active_player_abilities(self):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/activeplayerabilities', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
    #     return r
    
    # def get_active_player_runes(self):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/activeplayerrunes', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
    #     return r
    
    def get_all_players(self):
        r = requests.get(f'{self.lcu_url}:2999/liveclientdata/playerlist', headers={'Accept': '*/*'}, verify=f'{self.SSL_cert}')
        # print(r.json())
        return r
    
    # def get_target_player_scores(self, targetPlayer):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/playerscores?summonerName={targetPlayer}', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
    #     return r
    
    def get_target_player_summoner_spells(self, targetPlayer):
        r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/playersummonerspells?summonerName={targetPlayer}', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
        return r
    
    # def get_target_player_basic_runes(self, targetPlayer):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/playermainrunes?summonerName={targetPlayer}')
    #     return r
    
    def get_target_player_items(self, targetPlayer):
        r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/playeritems?summonerName={targetPlayer}', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
        return r
    
    # def get_events(self):
    #     r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/eventdata', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
    #     return r
    
    def get_game_stats(self):
        r = requests.get(f'{self.lcu_url}:{self.port}/liveclientdata/gamestats', headers={'Accept': 'application/json', 'Authorization': f'Basic {self.auth_key}'}, verify=f'{self.SSL_cert}')
        return r
    
class SpellTracker:
    def fetch_data_dragon_relevant_data(self):
        lol_watcher = LolWatcher(self.riot_dev_key)
        dd_versions = lol_watcher.data_dragon.versions_for_region('oce')
        dd_rune_data = lol_watcher.data_dragon.runes_reforged(dd_versions['v'])
        dd_summoner_spells_data = lol_watcher.data_dragon.summoner_spells(dd_versions['v'])
        return dd_rune_data, dd_summoner_spells_data

    def parse_runeIDs_for_inspiration_ID(self, dd_rune_IDs):
        for runeTree in dd_rune_IDs:
            if 'Inspiration' in runeTree['key']:
                inspiration_ID = runeTree['id']
                break
        return inspiration_ID

    def parse_runeIDs_for_CI_ID(self, dd_rune_IDs):
        CI_key = 'CosmicInsight'

        for i in range(len(dd_rune_IDs)):
            if 'Inspiration' in dd_rune_IDs[i]['key']:
                inspiration_tree_index = i
                break

        inspiration_slots = dd_rune_IDs[inspiration_tree_index]['slots']
        for row in range(len(inspiration_slots)):
            for rune in range(len(inspiration_slots[row]['runes'])):
                if CI_key in inspiration_slots[row]['runes'][rune]['key']:
                    return inspiration_slots[row]['runes'][rune]['id']
        
    async def fetch_summoner(self, api_key):
    #get my 
        async with RiotAPIClient(default_headers={"X-Riot-Token" : api_key}) as client:
            account = await client.get_account_v1_by_riot_id(region='asia', game_name='Shiva', tag_line='1920')
            summoner = await client.get_lol_summoner_v4_by_puuid(region='oc1', puuid=account['puuid'])
        return summoner

    async def fetch_active_game(self, api_key, summoner):
        async with RiotAPIClient(default_headers={"X-Riot-Token" : api_key}) as client:
            active_game = None
            try:
                active_game = await client.get_lol_spectator_v5_active_game_by_summoner(region='oc1', puuid=summoner['puuid'])
            except aiohttp.ClientResponseError as e:
                if e.status == 404: 
                    sys.exit('Error 404: Summoner not in a game')
                elif e.status == 401: 
                    sys.exit('Error 401: Invalid API Key. Generate a new one at https://developer.riotgames.com')
                elif e.status == 403:
                    sys.exit('Error 403: Forbidden')
                else:
                    sys.exit(e)
        return active_game

    def get_player_list(self, lcu):
        player_list = lcu.get_all_players().json()
        return player_list

    def get_game_time(self, lcu):
        game_time = lcu.get_game_stats().json()['gameTime']
        return game_time
    
    def get_game_mode(self, lcu):
        game_mode = lcu.get_game_stats().json()['gameMode']
        return game_mode

    def get_my_team(self, my_summoner_name, player_list):
        for player in player_list:
            if player['summonerName'] in my_summoner_name:
                my_team = player['team']
                break
        return my_team

    def get_enemy_list(self, my_team, player_list):
        enemy_list = []
        for player in player_list:
            if my_team not in player['team']:
                enemy_list.append(player)
            if (len(enemy_list) >= 5 ):
                break
        return enemy_list

    def get_summoner_haste_sources_list(self, enemy):
        summoner_haste_sources = {}
        if 'Ionian Boots of Lucidity' in enemy['items']:
            summoner_haste_sources['Ionian Boots of Lucidity'] = True
        else:
            summoner_haste_sources['Ionian Boots of Lucidity'] = False

        if 'Dawncore' in enemy['items']:
            summoner_haste_sources['Dawncore'] = True
        else:
            summoner_haste_sources['Dawncore'] = False
        
        if self.inspiration_ID in enemy['runes']['primaryRuneTree'] or self.inspiration_ID in enemy['runes']['secondaryRuneTree']:
            summoner_haste_sources['Inspiration'] = True
        else:
            summoner_haste_sources['Inspiration'] = False

        if self.game_mode == 'ARAM':
            summoner_haste_sources['ARAM'] = True
        else:
            summoner_haste_sources['ARAM'] = False
        
        return summoner_haste_sources

    def get_relevent_enemy_data_dict(self, enemy):
        new_dict = {}
        new_dict['summonerName'] = enemy['summonerName']
        new_dict['championName'] = enemy['championName']
        new_dict['level'] = enemy['level']
    
        new_dict['summonerSpells'] = enemy['summonerSpells']
        for key, summoner_spell in new_dict['summonerSpells'].items():
            spell_name = summoner_spell['displayName']
            summoner_spell = {}
            summoner_spell['name'] = spell_name
            new_dict['summonerSpells'][key] = summoner_spell

            if 'Teleport' in summoner_spell['name']:
                summoner_spell['name'] = 'Teleport'

        new_dict['summonerHasteSources'] = self.get_summoner_haste_sources_list(enemy)
        return new_dict

    def simplify_enemy_list(self, enemy_list):
        new_enemy_list = []
        for enemy in enemy_list:
            new_enemy_list.append(self.get_relevent_enemy_data_dict(enemy))
        return new_enemy_list

    # def get_enemies_with_inspiration(self, enemy_list):
    #     enemies_with_inspiration = []
    #     for enemy in enemy_list:
    #         if enemy['summonerHasteSources']['Inspiration']:
    #             enemies_with_inspiration.append(enemy)
    #     return enemies_with_inspiration
    
    # def check_for_Cosmic_Insight(self, enemies_with_inspiration, active_game):
    #     checklist = []
    #     for enemy in enemies_with_inspiration:
    #         for participant in active_game['participants']:
    #             if participant['summonerName'] in enemy['summonerName']:
    #                 if self.cosmic_insight_ID in participant['perks']['perkIDs']:
    #                     checklist.append(True)
    #                 else:
    #                     checklist.append(False)
    #     return checklist
            
    # def update_enemies_with_cosmic_insight(self, enemies_with_inspiration, enemies_with_Cosmic_Insight_checklist):
    #     for i in range(len(enemies_with_inspiration)):
    #         enemies_with_inspiration[i]['summonerHasteSources']['Cosmic Insight'] = enemies_with_Cosmic_Insight_checklist[i]

    def check_for_cosmic_insight(self, enemy_list, active_game):
        for enemy in enemy_list:
            for participant in active_game['participants']:
                if enemy['summonerHasteSources']['Inspiration'] and participant['summonerName'] in enemy['summonerName']:
                    if self.cosmic_insight_ID in participant['perks']['perkIDs']:
                        enemy['summonerHasteSources']['Cosmic Insight'] = True
                    else:
                        enemy['summonerHasteSources']['Cosmic Insight'] = False
                else:
                    enemy['summonerHasteSources']['Cosmic Insight'] = False


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
            for summoner, value in dd_summoner_spells_data['data'].items():
                if value['name'] in summoner_spell_name and self.game_mode in value['modes']:
                    summoner_cooldown_dict[summoner_spell_name] = value['cooldown'][0]
        return summoner_cooldown_dict
    
    def update_all_enemies_base_summoner_cooldowns(self, enemy_list, summoner_cd_dict):
        for enemy in enemy_list:
            self.update_enemy_base_summoner_cooldowns(enemy, summoner_cd_dict)

    def update_enemy_base_summoner_cooldowns(self, enemy, summoner_cd_dict):
        for key, enemy_summoner_spell in enemy['summonerSpells'].items():
            for summoner_spell, cooldown in summoner_cd_dict.items():
                if enemy_summoner_spell['name'] in summoner_spell:
                    enemy_summoner_spell['baseCooldown'] = cooldown
                    enemy['summonerSpells'][key] = enemy_summoner_spell



    #TODO: Add logic for calculating cds for both summs for each enemy and add to their dict. Special handling for Teleport - match name in database -> name in game ('Teleport' in 'Unleashed Teleport'), if game time >= 10mins, cd = base - (10 x Level) min 240 (max lvl = 10)
    def update_enemy_summoner_spell_starting_cooldown(self, enemy):
        for key, summoner_spell in enemy['summonerSpells'].items():
            base_cooldown = summoner_spell['baseCooldown']
            if 'Teleport' in summoner_spell['name']:
                base_cooldown = self.enemy_teleport_base_cooldown(enemy, base_cooldown)
            summoner_spell['startingCooldown'] = self.starting_cooldown(base_cooldown, enemy['summonerHaste'])
            enemy['summonerSpells'][key] = summoner_spell

    def enemy_teleport_base_cooldown(self, enemy, base_cooldown):
        if (self.game_time) >= 600:
            return base_cooldown - (10 * min(enemy['level'], 10))
        return base_cooldown
        
    def starting_cooldown(self, base_cooldown, haste):
        return (base_cooldown * (100/(100 + haste)))

    def calculate_enemy_summoner_cooldowns(self):
        for enemy in self.enemy_list:
            self.calculate_enemy_summoner_haste(enemy)
            self.update_enemy_summoner_spell_starting_cooldown(enemy)

    def __init__(self):
        load_dotenv()
        self.riot_dev_key = getenv('RIOT_DEV_API_KEY')
        self.my_region = 'OC1'
        self.my_summoner_name = getenv('SUMMONER_NAME')
        self.summoner_haste_sources = {
            "Ionian Boots of Lucidity": 12,
            "Dawncore": 18,
            "Cosmic Insight": 18,
            "ARAM": 70,
        }

    def main(self):
        lcu = LCU()

        rune_data, summoner_spell_data = self.fetch_data_dragon_relevant_data()

        self.inspiration_ID = self.parse_runeIDs_for_inspiration_ID(rune_data)
        self.cosmic_insight_ID = self.parse_runeIDs_for_CI_ID(rune_data)

        summoner = asyncio.run(self.fetch_summoner(self.riot_dev_key))
        active_game = asyncio.run(self.fetch_active_game(self.riot_dev_key, summoner))

        player_list = self.get_player_list(lcu)
        self.game_time = self.get_game_time(lcu)
        self.game_mode = self.get_game_mode(lcu)
        my_team = self.get_my_team(self.my_summoner_name, player_list)
        
        self.enemy_list = self.get_enemy_list(my_team, player_list)
        self.enemy_list = self.simplify_enemy_list(self.enemy_list)
        
        # enemies_with_inspiration = self.get_enemies_with_inspiration(self.enemy_list)
        # enemies_with_Cosmic_Insight_checklist = self.check_for_Cosmic_Insight(enemies_with_inspiration, active_game)
        # self.update_enemies_with_cosmic_insight(enemies_with_inspiration, enemies_with_Cosmic_Insight_checklist)

        for enemy in self.enemy_list:
            enemy['summonerHasteSources']['Cosmic Insight'] = self.check_for_cosmic_insight(self.enemy_list, active_game)

        unique_summoner_spells = self.find_unique_summoner_spells(self.enemy_list)
        summoner_cd_dict = self.create_summoner_cooldown_dict(unique_summoner_spells, summoner_spell_data)
        
        self.update_all_enemies_base_summoner_cooldowns(self.enemy_list, summoner_cd_dict)
        
        self.calculate_enemy_summoner_cooldowns()

        print(self.enemy_list[0]['summonerSpells'])
        
    
def __init__():
    st = SpellTracker()
    st.main()


#API_Key_Link = 'https://developer.riotgames.com'
__init__()
#Use pulsefire for 1. current game data
#Use riot_watcher/data_dragon for 1. summoner spells, 2. items
#Use lcu for 1. all players data, 2. game time