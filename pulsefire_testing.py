#%% run_imports
import asyncio
import aiohttp
import sys
from os import getenv
from dotenv import load_dotenv
from pulsefire.clients import RiotAPIClient

#puuid = 4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg

async def fetch_summoner(api_key):
    #get my 
    async with RiotAPIClient(default_headers={"X-Riot-Token" : api_key}) as client:
        account = await client.get_account_v1_by_riot_id(region='asia', game_name='Shiva', tag_line='1920')
        summoner = await client.get_lol_summoner_v4_by_puuid(region='oc1', puuid=account['puuid'])
    return summoner

async def fetch_active_game(api_key, summoner):
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


def __init__():
    load_dotenv()
    riot_dev_key = getenv('RIOT_DEV_API_KEY')
    summoner = asyncio.run(fetch_summoner(riot_dev_key))
    active_game = asyncio.run(fetch_active_game(riot_dev_key, summoner))
    
# asyncio.run(main())
# await main()

__init__()
# %%