from app.knight import Knight
from app.equipment import Armour, Weapon, Potion


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp <= 0:
        first_knight.hp = 0
    if second_knight.hp <= 0:
        second_knight.hp = 0


def battle(knights_config: list) -> dict:
    # BATTLE PREPARATIONS:

    knights = {}

    for kn in knights_config:
        knights[kn] = Knight(
            name=knights_config[kn]["name"],
            power=knights_config[kn]["power"],
            hp=knights_config[kn]["hp"],
        )

        for ar in knights_config[kn]["armour"]:
            knights[kn].equip_armour(Armour(ar["part"], ar["protection"]))

        knights[kn].equip_weapon(Weapon(
            name=knights_config[kn]["weapon"]["name"],
            power=knights_config[kn]["weapon"]["power"],
        ))

        if knights_config[kn]["potion"] is not None:
            knights[kn].drink_potion(Potion(
                name=knights_config[kn]["potion"]["name"],
                effect=knights_config[kn]["potion"]["effect"],
            ))

    # -------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(knights["lancelot"], knights["mordred"])

    # 2 Arthur vs Red Knight:
    fight(knights["arthur"], knights["red_knight"])

    return {
        knights[kn].name : knights[kn].hp for kn in knights
    }
