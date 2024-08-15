class FakeLCU:

    def __init__(self, alt: bool = False):
        if not alt:
            self.all_game_data = {
                "activePlayer": {
                    "abilities": {
                        "E": {
                            "abilityLevel": 0,
                            "displayName": "Wild Rush",
                            "id": "SamiraE",
                            "rawDescription": "GeneratedTip_Spell_SamiraE_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraE_DisplayName"
                        },
                        "Passive": {
                            "displayName": "Daredevil Impulse",
                            "id": "SamiraPassive",
                            "rawDescription": "GeneratedTip_Passive_SamiraPassive_Description",
                            "rawDisplayName": "GeneratedTip_Passive_SamiraPassive_DisplayName"
                        },
                        "Q": {
                            "abilityLevel": 0,
                            "displayName": "Flair",
                            "id": "SamiraQ",
                            "rawDescription": "GeneratedTip_Spell_SamiraQ_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraQ_DisplayName"
                        },
                        "R": {
                            "abilityLevel": 0,
                            "displayName": "Inferno Trigger",
                            "id": "SamiraR",
                            "rawDescription": "GeneratedTip_Spell_SamiraR_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraR_DisplayName"
                        },
                        "W": {
                            "abilityLevel": 0,
                            "displayName": "Blade Whirl",
                            "id": "SamiraW",
                            "rawDescription": "GeneratedTip_Spell_SamiraW_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraW_DisplayName"
                        }
                    },
                    "championStats": {
                        "abilityHaste": 8.0,
                        "abilityPower": 0.0,
                        "armor": 26.0,
                        "armorPenetrationFlat": 0.0,
                        "armorPenetrationPercent": 1.0,
                        "attackDamage": 62.400001525878909,
                        "attackRange": 500.0,
                        "attackSpeed": 0.6579999923706055,
                        "bonusArmorPenetrationPercent": 1.0,
                        "bonusMagicPenetrationPercent": 1.0,
                        "critChance": 0.0,
                        "critDamage": 175.0,
                        "currentHealth": 640.0,
                        "healShieldPower": 0.0,
                        "healthRegenRate": 0.6499999761581421,
                        "lifeSteal": 0.0,
                        "magicLethality": 0.0,
                        "magicPenetrationFlat": 0.0,
                        "magicPenetrationPercent": 1.0,
                        "magicResist": 30.0,
                        "maxHealth": 640.0,
                        "moveSpeed": 360.0,
                        "omnivamp": 0.0,
                        "physicalLethality": 0.0,
                        "physicalVamp": 0.0,
                        "resourceMax": 349.0,
                        "resourceRegenRate": 1.6399999856948853,
                        "resourceType": "MANA",
                        "resourceValue": 349.0,
                        "spellVamp": 0.0,
                        "tenacity": 5.0
                    },
                    "currentGold": 200.0,
                    "fullRunes": {
                        "generalRunes": [
                            {
                                "displayName": "Arcane Comet",
                                "id": 8229,
                                "rawDescription": "perk_tooltip_ArcaneComet",
                                "rawDisplayName": "perk_displayname_ArcaneComet"
                            },
                            {
                                "displayName": "Manaflow Band",
                                "id": 8226,
                                "rawDescription": "perk_tooltip_8226",
                                "rawDisplayName": "perk_displayname_8226"
                            },
                            {
                                "displayName": "Transcendence",
                                "id": 8210,
                                "rawDescription": "perk_tooltip_Transcendence",
                                "rawDisplayName": "perk_displayname_Transcendence"
                            },
                            {
                                "displayName": "Gathering Storm",
                                "id": 8236,
                                "rawDescription": "perk_tooltip_GatheringStorm",
                                "rawDisplayName": "perk_displayname_GatheringStorm"
                            },
                            {
                                "displayName": "Presence of Mind",
                                "id": 8009,
                                "rawDescription": "perk_tooltip_PresenceOfMind",
                                "rawDisplayName": "perk_displayname_PresenceOfMind"
                            },
                            {
                                "displayName": "Coup de Grace",
                                "id": 8014,
                                "rawDescription": "perk_tooltip_CoupDeGrace",
                                "rawDisplayName": "perk_displayname_CoupDeGrace"
                            }
                        ],
                        "keystone": {
                            "displayName": "Arcane Comet",
                            "id": 8229,
                            "rawDescription": "perk_tooltip_ArcaneComet",
                            "rawDisplayName": "perk_displayname_ArcaneComet"
                        },
                        "primaryRuneTree": {
                            "displayName": "Sorcery",
                            "id": 8200,
                            "rawDescription": "perkstyle_tooltip_7202",
                            "rawDisplayName": "perkstyle_displayname_7202"
                        },
                        "secondaryRuneTree": {
                            "displayName": "Precision",
                            "id": 8000,
                            "rawDescription": "perkstyle_tooltip_7201",
                            "rawDisplayName": "perkstyle_displayname_7201"
                        },
                        "statRunes": [
                            {
                                "id": 5007,
                                "rawDescription": "perk_tooltip_StatModCooldownReductionScaling"
                            },
                            {
                                "id": 5008,
                                "rawDescription": "perk_tooltip_StatModAdaptive"
                            },
                            {
                                "id": 5001,
                                "rawDescription": "perk_tooltip_StatModHealthScaling"
                            }
                        ]
                    },
                    "level": 1,
                    "riotId": "Shiva#1920",
                    "riotIdGameName": "Shiva",
                    "riotIdTagLine": "1920",
                    "summonerName": "Shiva#1920",
                    "teamRelativeColors": True
                },
                "allPlayers": [
                    {
                        "championName": "Samira",
                        "isBot": False,
                        "isDead": False,
                        "items": [
                            {
                                "canUse": False,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Boots",
                                "itemID": 1001,
                                "price": 300,
                                "rawDescription": "GeneratedTip_Item_1001_Description",
                                "rawDisplayName": "Item_1001_Name",
                                "slot": 0
                            },
                            {
                                "canUse": True,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Stealth Ward",
                                "itemID": 3340,
                                "price": 0,
                                "rawDescription": "GeneratedTip_Item_3340_Description",
                                "rawDisplayName": "Item_3340_Name",
                                "slot": 6
                            }
                        ],
                        "level": 1,
                        "position": "",
                        "rawChampionName": "game_character_displayname_Samira",
                        "rawSkinName": "game_character_skin_displayname_Samira_9",
                        "respawnTimer": 0.0,
                        "riotId": "Shiva#1920",
                        "riotIdGameName": "Shiva",
                        "riotIdTagLine": "1920",
                        "runes": {
                            "keystone": {
                                "displayName": "Arcane Comet",
                                "id": 8229,
                                "rawDescription": "perk_tooltip_ArcaneComet",
                                "rawDisplayName": "perk_displayname_ArcaneComet"
                            },
                            "primaryRuneTree": {
                                "displayName": "Sorcery",
                                "id": 8200,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 9,
                        "skinName": "PsyOps Samira",
                        "summonerName": "Shiva#1920",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Teleport",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerTeleport_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerTeleport_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerFlash_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerFlash_DisplayName"
                            }
                        },
                        "team": "ORDER"
                    },
                    {
                        "championName": "Tristana",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Tristana",
                        "respawnTimer": 0.0,
                        "riotId": "Tristana#BOT",
                        "riotIdGameName": "Tristana",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Tristana#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Heal",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Dr. Mundo",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_DrMundo",
                        "respawnTimer": 0.0,
                        "riotId": "DrMundo#BOT",
                        "riotIdGameName": "DrMundo",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Grasp of the Undying",
                                "id": 8437,
                                "rawDescription": "perk_tooltip_GraspOfTheUndying",
                                "rawDisplayName": "perk_displayname_GraspOfTheUndying"
                            },
                            "primaryRuneTree": {
                                "displayName": "Resolve",
                                "id": 8400,
                                "rawDescription": "perkstyle_tooltip_7204",
                                "rawDisplayName": "perkstyle_displayname_7204"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "DrMundo#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Heal",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Kayle",
                        "isBot": True,
                        "isDead": False,
                        "items": [
                            {
                                "canUse": False,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Ionian Boots of Lucidity",
                                "itemID": 3158,
                                "price": 350,
                                "rawDescription": "GeneratedTip_Item_3158_Description",
                                "rawDisplayName": "Item_3158_Name",
                                "slot": 0
                            },
                            {
                                "canUse": True,
                                "consumable": True,
                                "count": 1,
                                "displayName": "Health Potion",
                                "itemID": 2003,
                                "price": 50,
                                "rawDescription": "GeneratedTip_Item_2003_Description",
                                "rawDisplayName": "Item_2003_Name",
                                "slot": 1
                            },
                            {
                                "canUse": True,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Stealth Ward",
                                "itemID": 3340,
                                "price": 0,
                                "rawDescription": "GeneratedTip_Item_3340_Description",
                                "rawDisplayName": "Item_3340_Name",
                                "slot": 6
                            }
                        ],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Kayle",
                        "respawnTimer": 0.0,
                        "riotId": "Kayle#BOT",
                        "riotIdGameName": "Kayle",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Kayle#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Ghost",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Kog'Maw",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_KogMaw",
                        "respawnTimer": 0.0,
                        "riotId": "KogMaw#BOT",
                        "riotIdGameName": "KogMaw",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "KogMaw#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Barrier",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Ignite",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Jax",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Jax",
                        "respawnTimer": 0.0,
                        "riotId": "Jax#BOT",
                        "riotIdGameName": "Jax",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Jax#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Exhaust",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Cleanse",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    }
                ],
                "events": {
                    "Events": [
                        {
                            "EventID": 0,
                            "EventName": "GameStart",
                            "EventTime": 0.01897200010716915
                        }
                    ]
                },
                "gameData": {
                    "gameMode": "CLASSIC",
                    "gameTime": 595,
                    "mapName": "Map11",
                    "mapNumber": 11,
                    "mapTerrain": "Default"
                }
            }
        else:
            self.all_game_data = {
                "activePlayer": {
                    "abilities": {
                        "E": {
                            "abilityLevel": 0,
                            "displayName": "Wild Rush",
                            "id": "SamiraE",
                            "rawDescription": "GeneratedTip_Spell_SamiraE_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraE_DisplayName"
                        },
                        "Passive": {
                            "displayName": "Daredevil Impulse",
                            "id": "SamiraPassive",
                            "rawDescription": "GeneratedTip_Passive_SamiraPassive_Description",
                            "rawDisplayName": "GeneratedTip_Passive_SamiraPassive_DisplayName"
                        },
                        "Q": {
                            "abilityLevel": 0,
                            "displayName": "Flair",
                            "id": "SamiraQ",
                            "rawDescription": "GeneratedTip_Spell_SamiraQ_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraQ_DisplayName"
                        },
                        "R": {
                            "abilityLevel": 0,
                            "displayName": "Inferno Trigger",
                            "id": "SamiraR",
                            "rawDescription": "GeneratedTip_Spell_SamiraR_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraR_DisplayName"
                        },
                        "W": {
                            "abilityLevel": 0,
                            "displayName": "Blade Whirl",
                            "id": "SamiraW",
                            "rawDescription": "GeneratedTip_Spell_SamiraW_Description",
                            "rawDisplayName": "GeneratedTip_Spell_SamiraW_DisplayName"
                        }
                    },
                    "championStats": {
                        "abilityHaste": 8.0,
                        "abilityPower": 0.0,
                        "armor": 26.0,
                        "armorPenetrationFlat": 0.0,
                        "armorPenetrationPercent": 1.0,
                        "attackDamage": 62.400001525878909,
                        "attackRange": 500.0,
                        "attackSpeed": 0.6579999923706055,
                        "bonusArmorPenetrationPercent": 1.0,
                        "bonusMagicPenetrationPercent": 1.0,
                        "critChance": 0.0,
                        "critDamage": 175.0,
                        "currentHealth": 640.0,
                        "healShieldPower": 0.0,
                        "healthRegenRate": 0.6499999761581421,
                        "lifeSteal": 0.0,
                        "magicLethality": 0.0,
                        "magicPenetrationFlat": 0.0,
                        "magicPenetrationPercent": 1.0,
                        "magicResist": 30.0,
                        "maxHealth": 640.0,
                        "moveSpeed": 360.0,
                        "omnivamp": 0.0,
                        "physicalLethality": 0.0,
                        "physicalVamp": 0.0,
                        "resourceMax": 349.0,
                        "resourceRegenRate": 1.6399999856948853,
                        "resourceType": "MANA",
                        "resourceValue": 349.0,
                        "spellVamp": 0.0,
                        "tenacity": 5.0
                    },
                    "currentGold": 200.0,
                    "fullRunes": {
                        "generalRunes": [
                            {
                                "displayName": "Arcane Comet",
                                "id": 8229,
                                "rawDescription": "perk_tooltip_ArcaneComet",
                                "rawDisplayName": "perk_displayname_ArcaneComet"
                            },
                            {
                                "displayName": "Manaflow Band",
                                "id": 8226,
                                "rawDescription": "perk_tooltip_8226",
                                "rawDisplayName": "perk_displayname_8226"
                            },
                            {
                                "displayName": "Transcendence",
                                "id": 8210,
                                "rawDescription": "perk_tooltip_Transcendence",
                                "rawDisplayName": "perk_displayname_Transcendence"
                            },
                            {
                                "displayName": "Gathering Storm",
                                "id": 8236,
                                "rawDescription": "perk_tooltip_GatheringStorm",
                                "rawDisplayName": "perk_displayname_GatheringStorm"
                            },
                            {
                                "displayName": "Presence of Mind",
                                "id": 8009,
                                "rawDescription": "perk_tooltip_PresenceOfMind",
                                "rawDisplayName": "perk_displayname_PresenceOfMind"
                            },
                            {
                                "displayName": "Coup de Grace",
                                "id": 8014,
                                "rawDescription": "perk_tooltip_CoupDeGrace",
                                "rawDisplayName": "perk_displayname_CoupDeGrace"
                            }
                        ],
                        "keystone": {
                            "displayName": "Arcane Comet",
                            "id": 8229,
                            "rawDescription": "perk_tooltip_ArcaneComet",
                            "rawDisplayName": "perk_displayname_ArcaneComet"
                        },
                        "primaryRuneTree": {
                            "displayName": "Sorcery",
                            "id": 8200,
                            "rawDescription": "perkstyle_tooltip_7202",
                            "rawDisplayName": "perkstyle_displayname_7202"
                        },
                        "secondaryRuneTree": {
                            "displayName": "Precision",
                            "id": 8000,
                            "rawDescription": "perkstyle_tooltip_7201",
                            "rawDisplayName": "perkstyle_displayname_7201"
                        },
                        "statRunes": [
                            {
                                "id": 5007,
                                "rawDescription": "perk_tooltip_StatModCooldownReductionScaling"
                            },
                            {
                                "id": 5008,
                                "rawDescription": "perk_tooltip_StatModAdaptive"
                            },
                            {
                                "id": 5001,
                                "rawDescription": "perk_tooltip_StatModHealthScaling"
                            }
                        ]
                    },
                    "level": 1,
                    "riotId": "Shiva#1920",
                    "riotIdGameName": "Shiva",
                    "riotIdTagLine": "1920",
                    "summonerName": "Shiva#1920",
                    "teamRelativeColors": True
                },
                "allPlayers": [
                    {
                        "championName": "Samira",
                        "isBot": False,
                        "isDead": False,
                        "items": [
                            {
                                "canUse": False,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Boots",
                                "itemID": 1001,
                                "price": 300,
                                "rawDescription": "GeneratedTip_Item_1001_Description",
                                "rawDisplayName": "Item_1001_Name",
                                "slot": 0
                            },
                            {
                                "canUse": True,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Stealth Ward",
                                "itemID": 3340,
                                "price": 0,
                                "rawDescription": "GeneratedTip_Item_3340_Description",
                                "rawDisplayName": "Item_3340_Name",
                                "slot": 6
                            }
                        ],
                        "level": 1,
                        "position": "",
                        "rawChampionName": "game_character_displayname_Samira",
                        "rawSkinName": "game_character_skin_displayname_Samira_9",
                        "respawnTimer": 0.0,
                        "riotId": "Shiva#1920",
                        "riotIdGameName": "Shiva",
                        "riotIdTagLine": "1920",
                        "runes": {
                            "keystone": {
                                "displayName": "Arcane Comet",
                                "id": 8229,
                                "rawDescription": "perk_tooltip_ArcaneComet",
                                "rawDisplayName": "perk_displayname_ArcaneComet"
                            },
                            "primaryRuneTree": {
                                "displayName": "Sorcery",
                                "id": 8200,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 9,
                        "skinName": "PsyOps Samira",
                        "summonerName": "Shiva#1920",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Teleport",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerTeleport_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerTeleport_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerFlash_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerFlash_DisplayName"
                            }
                        },
                        "team": "ORDER"
                    },
                    {
                        "championName": "Kog'Maw",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_KogMaw",
                        "respawnTimer": 0.0,
                        "riotId": "KogMaw#BOT",
                        "riotIdGameName": "KogMaw",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "KogMaw#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Barrier",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Ignite",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Tristana",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Tristana",
                        "respawnTimer": 0.0,
                        "riotId": "Tristana#BOT",
                        "riotIdGameName": "Tristana",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Tristana#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Heal",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Kayle",
                        "isBot": True,
                        "isDead": False,
                        "items": [
                            {
                                "canUse": False,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Ionian Boots of Lucidity",
                                "itemID": 3158,
                                "price": 350,
                                "rawDescription": "GeneratedTip_Item_3158_Description",
                                "rawDisplayName": "Item_3158_Name",
                                "slot": 0
                            },
                            {
                                "canUse": True,
                                "consumable": True,
                                "count": 1,
                                "displayName": "Health Potion",
                                "itemID": 2003,
                                "price": 50,
                                "rawDescription": "GeneratedTip_Item_2003_Description",
                                "rawDisplayName": "Item_2003_Name",
                                "slot": 1
                            },
                            {
                                "canUse": True,
                                "consumable": False,
                                "count": 1,
                                "displayName": "Stealth Ward",
                                "itemID": 3340,
                                "price": 0,
                                "rawDescription": "GeneratedTip_Item_3340_Description",
                                "rawDisplayName": "Item_3340_Name",
                                "slot": 6
                            }
                        ],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Kayle",
                        "respawnTimer": 0.0,
                        "riotId": "Kayle#BOT",
                        "riotIdGameName": "Kayle",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Kayle#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Ghost",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Dr. Mundo",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_DrMundo",
                        "respawnTimer": 0.0,
                        "riotId": "DrMundo#BOT",
                        "riotIdGameName": "DrMundo",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Grasp of the Undying",
                                "id": 8437,
                                "rawDescription": "perk_tooltip_GraspOfTheUndying",
                                "rawDisplayName": "perk_displayname_GraspOfTheUndying"
                            },
                            "primaryRuneTree": {
                                "displayName": "Resolve",
                                "id": 8400,
                                "rawDescription": "perkstyle_tooltip_7204",
                                "rawDisplayName": "perkstyle_displayname_7204"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "DrMundo#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Flash",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Heal",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                    {
                        "championName": "Jax",
                        "isBot": True,
                        "isDead": False,
                        "items": [],
                        "level": 1,
                        "position": "TOP",
                        "rawChampionName": "game_character_displayname_Jax",
                        "respawnTimer": 0.0,
                        "riotId": "Jax#BOT",
                        "riotIdGameName": "Jax",
                        "riotIdTagLine": "BOT",
                        "runes": {
                            "keystone": {
                                "displayName": "Press the Attack",
                                "id": 8005,
                                "rawDescription": "perk_tooltip_PressTheAttack",
                                "rawDisplayName": "perk_displayname_PressTheAttack"
                            },
                            "primaryRuneTree": {
                                "displayName": "Precision",
                                "id": 8000,
                                "rawDescription": "perkstyle_tooltip_7201",
                                "rawDisplayName": "perkstyle_displayname_7201"
                            },
                            "secondaryRuneTree": {
                                "displayName": "Inspiration",
                                "id": 8300,
                                "rawDescription": "perkstyle_tooltip_7202",
                                "rawDisplayName": "perkstyle_displayname_7202"
                            }
                        },
                        "scores": {
                            "assists": 0,
                            "creepScore": 0,
                            "deaths": 0,
                            "kills": 0,
                            "wardScore": 0.0
                        },
                        "skinID": 0,
                        "summonerName": "Jax#BOT",
                        "summonerSpells": {
                            "summonerSpellOne": {
                                "displayName": "Exhaust",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                            },
                            "summonerSpellTwo": {
                                "displayName": "Cleanse",
                                "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                                "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                            }
                        },
                        "team": "CHAOS"
                    },
                ],
                "events": {
                    "Events": [
                        {
                            "EventID": 0,
                            "EventName": "GameStart",
                            "EventTime": 0.01897200010716915
                        }
                    ]
                },
                "gameData": {
                    "gameMode": "CLASSIC",
                    "gameTime": 550,
                    "mapName": "Map11",
                    "mapNumber": 11,
                    "mapTerrain": "Default"
                }
            }

    def get_all_players(self) -> dict:
        return self.all_game_data['allPlayers']

    def get_target_player_items(self, target_riot_id) -> dict:
        for player in self.all_game_data['allPlayers']:
            if player['riotId'] in target_riot_id:
                return player['items']
        assert False

    def get_game_stats(self) -> dict:
        return self.all_game_data['gameData']
