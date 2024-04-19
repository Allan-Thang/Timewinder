import requests
# import base64
# import wmi
# import os
from riotwatcher import LolWatcher, ApiError

class LCU:
    def __init__(self):
        self.install_directory = None
        self.port = None
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

    def load_start_data(self):
        self.port = '2999'

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
    def get_inspiration_ID(self):
        for runeTree in self.dd_rune_IDs:
            if 'Inspiration' in runeTree['key']:
                inspiration_ID = runeTree['id']
                break
        return inspiration_ID

    def get_CI_ID(self):
        CI_key = 'CosmicInsight'

        for i in range(len(self.dd_rune_IDs)):
            if 'Inspiration' in self.dd_rune_IDs[i]['key']:
                inspiration_tree_index = i
                break

        inspiration_slots = self.dd_rune_IDs[inspiration_tree_index]['slots']
        for row in range(len(inspiration_slots)):
            for rune in range(len(inspiration_slots[row]['runes'])):
                if CI_key in inspiration_slots[row]['runes'][rune]['key']:
                    return inspiration_slots[row]['runes'][rune]['id']
        
    def get_player_list(self):
        player_list = self.riot_endpoint.get_all_players().json()
        return player_list

    def get_my_summoner_name(self):
        active_player = self.riot_endpoint.get_active_player_data().json()
        my_summoner_name = active_player['summonerName']
        return my_summoner_name

    def get_game_time(self):
        game_time = self.riot_endpoint.get_game_stats().json()['gameTime']
        return game_time

    def get_my_team(self):
        for player in self.player_list:
            if player['summonerName'] in self.my_summoner_name:
                my_team = player['team']
                break
        return my_team

    def get_enemy_list(self):
        enemy_list = []
        for player in self.player_list:
            if self.my_team not in player['team']:
                enemy_list.append(player)
            if (len(enemy_list) >= 5 ):
                break
        return enemy_list

    def get_summoner_haste_sources_list(self, enemy):
        summoner_haste_sources = {}
        if 'Ionian Boots of Lucidity' in enemy['item']:
            summoner_haste_sources['Ionian Boots'] = True
        else:
            summoner_haste_sources['Ionian Boots'] = False

        if 'Dawncore' in enemy['items']:
            summoner_haste_sources['Dawncore'] = True
        else:
            summoner_haste_sources['Dawncore'] = False
        
        if self.inspiration_ID in enemy['runes']['primaryRuneTree'] or self.inspiration_ID in enemy['runes']['secondaryRuneTree']:
            summoner_haste_sources['Inspiration'] = True
        else:
            summoner_haste_sources['Inspiration'] = False

    def get_relevent_enemy_data_dict(self, enemy):
        new_dict = {}
        new_dict['summonerName'] = enemy['summonerName']
        new_dict['championName'] = enemy['championName']
        new_dict['level'] = enemy['level']
        new_dict['summonerSpells'] = enemy['summonerSpells']
        new_dict['summonerHasteSources'] = self.get_summoner_haste_sources_list(enemy)
        return new_dict

    def simplify_enemy_list(self):
        new_enemy_list = []
        for enemy in self.enemy_list:
            new_enemy_list.append(self.get_relevent_enemy_data_dict(enemy))
        return new_enemy_list

    def get_enemies_with_inspiration(self):
        enemies_with_inspiration = []
        for enemy in self.enemy_list:
            if enemy['summonerHasteSources']['Inspiration']:
                enemies_with_inspiration.append(enemy)
        return enemies_with_inspiration
    
    def check_for_Cosmic_Insight(self):
        checklist = []
        for enemy in self.enemies_with_inspiration:
            for participant in self.game['participants']:
                if participant['summonerName'] in enemy['summonerName']:
                    if self.cosmic_insight_ID in participant['perks']['perkIDs']:
                        checklist.append(True)
                    else:
                        checklist.append(False)
        return checklist
            
    def update_summoner_haste_sources(self):
        for i in len(self.enemies_with_inspiration):
            self.enemies_with_inspiration[i]['summonerHasteSources']['Cosmic Insight'] = self.enemies_with_Cosmic_Insight_checklist[i]

    def calculate_enemy_summoner_haste(self):
        for enemy in self.enemy_list:
            summoner_haste = 0
            for source in self.summoner_haste_sources:
                if enemy['summonerHasteSources'][source]:
                    summoner_haste += self.summoner_haste_sources[source]
            enemy['summonerHaste'] = summoner_haste

    def find_unique_summoner_spells(self):
        summoner_list = {}
        for enemy in self.enemy_list:
            for summoner_spell in enemy['summonerSpells']:
                if summoner_spell['displayName'] not in summoner_list:
                    summoner_list[summoner_spell['displayName']] = 0
        return summoner_list
                
    def create_summoner_cooldown_dict(self):
        summoner_cooldown_dict = {}
        for summoner_spell in self.unique_summoner_spells:
            for summoner, value in self.dd_summoner_spells_data['data'].items():
                if summoner_spell in value['name'] and 'CLASSIC' in value['modes']:
                    summoner_cooldown_dict[summoner_spell] = value['cooldown'][0]



    def __init__(self):
        my_region = 'OC1'
        self.my_summoner_name = 'Shiva'
        self.lol_watcher = LolWatcher('RGAPI-0001a48a-e26e-4cd8-a90e-6a0456bac323')
        self.summoner_haste_sources = {
            "Ionian Boots of Lucidity": 12,
            "Dawncore": 18,
            "Cosmic Insight": 18
        }
        
        self.lcu = LCU()
        self.lcu.load_start_data()

        self.dd_versions = self.lol_watcher.data_dragon.versions_for_region('oce')

        self.dd_rune_IDs = self.lol_watcher.data_dragon.runes_reforged(self.dd_versions['v'])
        self.inspiration_ID = self.get_inspiration_ID()
        self.cosmic_insight_ID = self.get_CI_ID()

        self.me = self.lol_watcher.summoner.by_name(my_region, self.my_summoner_name)
        self.game = self.lol_watcher.spectator.by_summoner(my_region, self.me['id'])
        self.dd_summoner_spells_data = self.lol_watcher.data_dragon.summoner_spells(self.dd_versions['v'])


        self.player_list = self.get_player_list()
        self.my_summoner_name = self.get_my_summoner_name()
        self.game_time = self.get_game_time()
        self.my_team = self.get_my_team()
        self.enemy_list = self.get_enemy_list()
        self.enemy_list = self.simplify_enemy_list()
        self.enemies_with_inspiration = self.get_enemies_with_inspiration()
        self.enemies_with_Cosmic_Insight_checklist = self.check_for_Cosmic_Insight()
        self.do_enemies_have_Cosmic_Insight = self.check_for_Cosmic_Insight()
        self.update_summoner_haste_sources()
        self.calculate_enemy_summoner_haste()
        self.unique_summoner_spells = self.find_unique_summoner_spells()
        self.find_summoner_cooldowns()
    
def __init__():
    st = SpellTracker()


#API_Key_Link = 'https://developer.riotgames.com'
__init__()
#Use pulsefire for 1. current game data
#Use data_dragon for 1. summoner spells, 2. items