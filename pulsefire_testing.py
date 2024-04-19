import asyncio
import os
from dotenv import load_dotenv
from pulsefire.clients import RiotAPIClient, CDragonClient

api_key = 'RGAPI-5646abfd-72d9-44bf-a1b0-907adf5826f0'

#puuid = 4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg

#%% run_imports
async def main():
    #get my 
    async with RiotAPIClient(default_headers={"X-Riot-Token" : api_key}) as client:
        account = await client.get_account_v1_by_riot_id(region='asia', game_name='Shiva', tag_line='1920')
        summoner = await client.get_lol_summoner_v4_by_puuid(region='oc1', puuid=account['puuid'])
        active_game = await client.get_lol_spectator_v5_active_game_by_summoner(region='oc1', puuid=summoner['puuid'])
        # print(active_game)

def store_api_key():
    print(os.environ)



# asyncio.run(main())
# await main()
# %%