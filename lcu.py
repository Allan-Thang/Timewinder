import requests

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