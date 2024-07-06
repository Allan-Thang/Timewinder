from threading import Event
from typing import Any, TypedDict


class Enemy(TypedDict):
    riot_id: str
    champion_name: str
    level: int
    items: list[str]
    champion_icon: bytes
    summoner_spells: dict
    summoner_haste_sources: dict
    summoner_haste: int


class Cooldown(TypedDict):
    name: str
    cooldown: float
    thread: Any
    stop: Event
