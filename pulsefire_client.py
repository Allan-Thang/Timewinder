# %% run_imports
import asyncio
import sys
from os import getenv

import aiohttp
import requests
from dotenv import load_dotenv
from pulsefire.clients import CDragonClient, RiotAPIClient

# puuid = 4TpQ_LY5CQDij-Qi8UjOtM4I61M4HqGVXfY1bXi66MM4UpdeyuWnWKk7eFvZD5ESH659NcmEWBP0Wg


class PulsefireClient():

    def __init__(self, riot_dev_key=str(getenv('RIOT_DEV_API_KEY'))):
        load_dotenv()
        self.riot_dev_key = riot_dev_key
        # summoner = asyncio.run(fetch_summoner(riot_dev_key))
        # active_game = asyncio.run(fetch_active_game(riot_dev_key, summoner))
        self.champion_summary = asyncio.run(self.fetch_champion_data())
        self.summoner_spells = asyncio.run(self.fetch_summoner_spells())

        # print(champion_summary)

    async def fetch_summoner(self, region: str = 'asia', server: str = 'oc1', game_name: str = 'Shiva', tag_line: str = '1920'):
        # get my
        async with RiotAPIClient(default_headers={"X-Riot-Token": self.riot_dev_key}) as client:
            account = await client.get_account_v1_by_riot_id(region=region, game_name=game_name, tag_line=tag_line)
            summoner = await client.get_lol_summoner_v4_by_puuid(region=server, puuid=account['puuid'])
        return summoner

    async def fetch_active_game(self, summoner):
        async with RiotAPIClient(default_headers={"X-Riot-Token": self.riot_dev_key}) as client:
            active_game = None
            try:
                active_game = await client.get_lol_spectator_v5_active_game_by_summoner(region='oc1', puuid=summoner['puuid'])
            except aiohttp.ClientResponseError as e:
                if e.status == 404:
                    sys.exit('Error 404: Summoner not in a game')
                elif e.status == 401:
                    sys.exit(
                        'Error 401: Invalid API Key. Generate a new one at https://developer.riotgames.com')
                elif e.status == 403:
                    sys.exit('Error 403: Forbidden')
                else:
                    sys.exit(f'{e}')
        return active_game

    async def fetch_champion_data(self):
        async with CDragonClient(default_params={"patch": "latest", "locale": "en_au"}) as client:
            champion_summary = await client.get_lol_v1_champion_summary()

        return champion_summary

    def fetch_champ_icon(self, champ_name: str) -> bytes:
        for champion in self.champion_summary:
            if champ_name in champion['name']:
                champ_id = champion['id']
                base_url = 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/'
                r = requests.get(f'{base_url}{str(champ_id)}.png', timeout=5)
                icon = r.content
                return icon
        assert False

    async def fetch_summoner_spells(self):
        async with CDragonClient(default_params={"patch": "latest", "locale": "en_au"}) as client:
            summoner_spells = await client.get_lol_v1_summoner_spells()
        return summoner_spells

    def fetch_summoner_spell_icon(self, summoner_spell_name: str) -> bytes:
        for summoner_spell in self.summoner_spells:
            if summoner_spell_name in summoner_spell['name']:
                file_name = summoner_spell['iconPath'].split('/')[-1].lower()
                base_url = 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/data/spells/icons2d/'
                r = requests.get(f'{base_url}{str(file_name)}', timeout=5)
                icon = r.content
                return icon
        assert False

# asyncio.run(main())
# await main()


def main():
    load_dotenv()
    dev_key = str(getenv('RIOT_DEV_API_KEY'))
    pf = PulsefireClient(dev_key)
    asyncio.run(pf.fetch_summoner())
    # summoner_spells = asyncio.run(pf.fetch_summoner_spells())
    # file_name = pf.fetch_summoner_spell_icon('Cleanse')
    # print(summoner_spells)
    # image = pf.fetch_champ_image('Zoe')
    # print(image)


if __name__ == '__main__':
    main()
# %%
