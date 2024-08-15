import tkinter as tk
from threading import Event
from tkinter import ttk
from typing import Any, NotRequired, TypedDict


class SummonerSpellData(TypedDict):
    name: str
    base_cooldown: float
    starting_cooldown: float
    icon: bytes


class EnemyData(TypedDict):
    riot_id: str
    champion_name: str
    level: int
    items: list[str]
    champion_icon: bytes
    summoner_spells: list[SummonerSpellData]
    summoner_haste_sources: dict[str, bool]
    summoner_haste: int


class CooldownData(TypedDict):
    champion_name: str
    spell_name: str
    on_cooldown: bool
    start_time: float
    starting_cooldown: float
    remaining_time: float
    widget: Any


class RowWidgets(TypedDict):
    row: tk.Frame
    champion_image: ttk.Label
    champion_name: str
    summoner_spell_one_image: tk.Button
    summoner_spell_one_cooldown: ttk.Label
    summoner_spell_two_image: tk.Button
    summoner_spell_two_cooldown: ttk.Label
    move_row_up_button: ttk.Button
    move_row_down_button: ttk.Button
    enemy: EnemyData | None
