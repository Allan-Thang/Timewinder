from riotwatcher import LolWatcher, ApiError
import requests
from pulsefire.clients import RiotAPIClient

game = {
    "gameId": 618090225,
    "mapId": 12,
    "gameMode": "ARAM",
    "gameType": "MATCHED",
    "gameQueueConfigId": 450,
    "participants": [
        {
            "puuid": "ZpMVfmniOfZgZTdJG3tDDK-UR-mmAqbFp4ecv8UExGKyDCpov_ETBVEEodh6yxL_yQuDDhoR_IuIiQ",
            "teamId": 100,
            "spell1Id": 32,
            "spell2Id": 4,
            "championId": 268,
            "profileIconId": 5655,
            "summonerName": "Suck My Boba",
            "riotId": "Hopium#5015",
            "bot": 0,
            "summonerId": "gYefR22bDIVy5FWD1e4zQ7a5Vx8ZWwpkFFzpjAdIOFln",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8008,
                    9111,
                    9105,
                    8014,
                    8429,
                    8451,
                    5007,
                    5001,
                    5001
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8400
            }
        },
        {
            "puuid": "pWwoRY4KUoARTttXSdmwV7ckYps4lghXpUQG-SY78HjhY93o1UY7ELhJWLwHe3Im3XaU-NdRstnBVw",
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 3,
            "championId": 63,
            "profileIconId": 4765,
            "summonerName": "El gay guy ",
            "riotId": "Onision#1468",
            "bot": 0,
            "summonerId": "kNaD3xSvCqETbSficRL1eLxaa-tcNygedaGeD_L9mQDS9g",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8229,
                    8226,
                    8210,
                    8237,
                    8135,
                    8138,
                    5008,
                    5010,
                    5001
                ],
                "perkStyle": 8200,
                "perkSubStyle": 8100
            }
        },
        {
            "puuid": "zDr_Y13qweGFMg7vEKyMdQomqRCOPSoPAibPT2_X-bdvOICYbvMQJMfYxMWGQ8kSpP4p8ES-vPxFGA",
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 6,
            "championId": 122,
            "profileIconId": 5757,
            "summonerName": "Silent Midnight",
            "riotId": "Silent Midnight#OCE",
            "bot": 0,
            "summonerId": "PfBxvhunW1MDVUEs2ciZVEORUGZzVTnTz7vuXulaeVmjfA",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8437,
                    8401,
                    8444,
                    8347,
                    8134,
                    8138,
                    5005,
                    5001,
                    5001
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8100
            }
        },
        {
            "puuid": "TNnZnkVCQ6svqmQKFRSEetTJGC0KuPXS7xr7SnMI6wvWA7fWNGl0i1-2xDvFC0tM1152Mqp0Zfbsjg",
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 6,
            "championId": 35,
            "profileIconId": 5184,
            "summonerName": "Lady killer Nico",
            "riotId": "Lady killer Nico#OCE",
            "bot": 0,
            "summonerId": "zPaZn089HVu_c9e_MdOUPxCDECZ_SP3sa327W4bxmgYL-g",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    9923,
                    8143,
                    8138,
                    8135,
                    9111,
                    8299,
                    5005,
                    5008,
                    5001
                ],
                "perkStyle": 8100,
                "perkSubStyle": 8000
            }
        },
        {
            "puuid": "IWUPwcbsYFI5ylkyBPkVB02NM_kZQWr2Ne5hD-ikEbqO2JEP7EPbxCN_1tvMpHddOgmt7r8n-polvg",
            "teamId": 100,
            "spell1Id": 14,
            "spell2Id": 4,
            "championId": 127,
            "profileIconId": 4022,
            "summonerName": "Smelly Cat",
            "riotId": "Smelly Cat#OCE",
            "bot": 0,
            "summonerId": "F-AsckzEGlmcyVKWoHeIfrH4neun2Yy7muirrE_m82XmHT0",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8112,
                    8143,
                    8138,
                    8135,
                    8210,
                    8236,
                    5008,
                    5008,
                    5011
                ],
                "perkStyle": 8100,
                "perkSubStyle": 8200
            }
        },
        {
            "puuid": "FUaJ4nN89Qmvxvk5f3g3H7p8iVv7iaDAfh0WpedGU_IodFnIeMhVMFqVTaz9GmXehbHQV6YplG4oZg",
            "teamId": 200,
            "spell1Id": 4,
            "spell2Id": 6,
            "championId": 10,
            "profileIconId": 6526,
            "summonerName": "Onata",
            "riotId": "Onata#OCE",
            "bot": 0,
            "summonerId": "qvFMpOnuYsUmvNgXni7a7WQgV7s6nX1P1gS9GxYax83vtaCny5GB766GLw",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8008,
                    8009,
                    9104,
                    8017,
                    8313,
                    8345,
                    5005,
                    5008,
                    5013
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "puuid": "4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg",
            "teamId": 200,
            "spell1Id": 6,
            "spell2Id": 4,
            "championId": 950,
            "profileIconId": 4763,
            "summonerName": "Shiva",
            "riotId": "Shiva#1920",
            "bot": 0,
            "summonerId": "iDEAjex3RGRVwH6ObvpWS0DqFrCOHHo-1M3GlofkVuFh4A",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8112,
                    8143,
                    8138,
                    8135,
                    8009,
                    8014,
                    5008,
                    5008,
                    5001
                ],
                "perkStyle": 8100,
                "perkSubStyle": 8000
            }
        },
        {
            "puuid": "nrcP82XRi0yiYtpRpbNKq7cJydVmta8x33veiRERm2OGy7bjBo4hX_Pz-zcaQkue6eXjsAWhRctU0w",
            "teamId": 200,
            "spell1Id": 32,
            "spell2Id": 4,
            "championId": 254,
            "profileIconId": 4568,
            "summonerName": "Nheo Nheo",
            "riotId": "Nheo Nheo#OCE",
            "bot": 0,
            "summonerId": "p4ZA3nwrWmo-p_7EpCFcG6NP_VyFCSzxbpOKelfTIycv-IE",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    9923,
                    8143,
                    8138,
                    8135,
                    8014,
                    9111,
                    5005,
                    5008,
                    5001
                ],
                "perkStyle": 8100,
                "perkSubStyle": 8000
            }
        },
        {
            "puuid": "uo-5CsX4CA5S0WogaBOKyp5dSuS3Dw_RltU4_FlMvx4S8PbB0SQHoIYqlU13OnTFbR9lD0PkxdSQdw",
            "teamId": 200,
            "spell1Id": 4,
            "spell2Id": 32,
            "championId": 80,
            "profileIconId": 3546,
            "summonerName": "Thee MuffnMan",
            "riotId": "Thee MuffnMan#OCE",
            "bot": 0,
            "summonerId": "YXu3xg43U67rNlSJBsR_jZgKyzKrJY5ly6tQHIO3bHCSmQQ",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8010,
                    8009,
                    9105,
                    8299,
                    8143,
                    8135,
                    5008,
                    5008,
                    5013
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8100
            }
        },
        {
            "puuid": "WvfJW0em_Njxq1HsUsFpyTrYWlX9SpR7DKLK7MBQryLvOfgPpj2tbw41uHhot3k2Jpi-FEr_u2OWag",
            "teamId": 200,
            "spell1Id": 4,
            "spell2Id": 32,
            "championId": 57,
            "profileIconId": 691,
            "summonerName": "Sokrates",
            "riotId": "Sokrates#OCE",
            "bot": 0,
            "summonerId": "fJCDC1rn8XAt4eF5dn754oEfTM1gj16bQbNKM7WGhVQR",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8437,
                    8463,
                    8429,
                    8451,
                    8134,
                    8126,
                    5007,
                    5001,
                    5001
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8100
            }
        }
    ],
    "observers": {
        "encryptionKey": "hRoIV2L1BXoHwNWUlaF/inhs9rg4FX9N"
    },
    "platformId": "OC1",
    "bannedChampions": [],
    "gameStartTime": 1712303788339,
    "gameLength": 92
}

API_Key_Link = 'https://developer.riotgames.com'
my_region = 'OC1'
my_summoner_name = 'Shiva'
lol_watcher = LolWatcher('RGAPI-0001a48a-e26e-4cd8-a90e-6a0456bac323')


me = lol_watcher.summoner.by_name(my_region, my_summoner_name)

versions = lol_watcher.data_dragon.versions_for_region('oce')

items = lol_watcher.data_dragon.items(versions['v'])

# runes = lol_watcher.data_dragon.runes_reforged(versions['v'])

print('\n')
# ss = lol_watcher.data_dragon.summoner_spells(versions['v'])
# for summoner, data in ss['data'].items():
#     if 'Flash' in data['name'] and 'CLASSIC' in data['modes']:
#         print(data['cooldown'][0])

# print(items)
# print(runes)

# def get_inspiration_ID(runes):
#     for runeTree in runes:
#         if 'Inspiration' in runeTree['key']:
#             inspiration_ID = runeTree['id']
#             break
#     return inspiration_ID

# inspiration_ID = get_inspiration_ID(runes)
# print(inspiration_ID)

# def find_CI_ID(runes):
#     CI_rune_tree = 'Inspiration'
#     CI_key = 'CosmicInsight'

#     for i in range(len(runes)):
#         if CI_rune_tree in runes[i]['key']:
#             inspiration_tree_index = i
#             break

#     inspiration_slots = runes[inspiration_tree_index]['slots']
#     for row in range(len(inspiration_slots)):
#         for rune in range(len(inspiration_slots[row]['runes'])):
#             if CI_key in inspiration_slots[row]['runes'][rune]['key']:
#                 return inspiration_slots[row]['runes'][rune]['id']
    
# cosmic_insight_ID = find_CI_ID(runes)

# print('\n')
# print(f'Cosmic Insight ID = {cosmic_insight_ID}')

game = lol_watcher.spectator.by_summoner(my_region, me['id'])
riot_api_url = 'https://oc1.api.riotgames.com/lol'
spectator_url = 'spectator/v5/active-games/by-summoner'
puuid = '4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg'
api_key = 'RGAPI-0001a48a-e26e-4cd8-a90e-6a0456bac323'
# r = requests.get(f'{riot_api_url}/{spectator_url}/{puuid}?api_key={api_key}')
r = requests.get('https://oc1.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg?api_key=RGAPI-0001a48a-e26e-4cd8-a90e-6a0456bac323')
print(r.json())

        
# def ingame_find_me():
#     for participant in game['participants']:
#         if me['puuid'] in participant['puuid']:
#             return participant

# participant_me = ingame_find_me()
# print(f'\nMy ingame info = {participant_me}')

# def ingame_find_my_teamId():
#     return participant_me['teamId']

# teamID = ingame_find_my_teamId()
# print(f'\nMy teamId = {teamID}')

# enemyTeamID = 200 if (teamID == 100) else 100

# print(f'\nEnemyTeamID = {enemyTeamID}')

# def create_list_of_teams_players(team):
#     enemy_team_players_list = []
#     for participant in game['participants']:
#         if participant['teamId'] == enemyTeamID:
#             enemy_team_players_list.append(participant)
#     return enemy_team_players_list
# enemy_team_players_list = create_list_of_teams_players(enemyTeamID)
# print(f'\nEnemyTeamPlayersList = {enemy_team_players_list}')

# def ingame_check_if_players_have_cosmic_insight(player_list):
#     enemy_CI_checklist = []
#     for player in player_list:
#         has_CI = cosmic_insight_ID in player['perks']['perkIds']
#         enemy_CI_checklist.append(has_CI)
#     return enemy_CI_checklist
# enemy_CI_checklist = ingame_check_if_players_have_cosmic_insight(enemy_team_players_list)
# print(f'\nEnemy_CI_checklist = {enemy_CI_checklist}')

# def getChampList():
#     return lol_watcher.data_dragon.champions(versions['n']['champion'])
# champList = getChampList()
# # print('\nChampList = ', champList['data'])

# def championId_to_champion(champId, champList):
#     print(champId)
#     for iChampion in champList['data']:
#         # print(champList['data'][iChampion]['key'])
#         if champId == int(champList['data'][iChampion]['key']):
#             print('here)')
#             return champList['data'][iChampion]
        
# newChamp = championId_to_champion(516, champList)
# print(newChamp)