from knight import Knight
from equipment import Armour, Weapon, Potion


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp <= 0:
        first_knight.hp = 0
    if second_knight.hp <= 0:
        second_knight.hp = 0


def battle() -> dict:
    # BATTLE PREPARATIONS:

    # lancelot ----

    lancelot = Knight("Lancelot", power=35, hp=100)
    lancelot.equip_weapon(Weapon("Metal Sword", 50))

    # arthur ----

    arthur = Knight("Arthur", power=45, hp=75)
    arthur.equip_armour(Armour("helmet", 15))
    arthur.equip_armour(Armour("breastplate", 20))
    arthur.equip_armour(Armour("boots", 10))
    arthur.equip_weapon(Weapon("Two-handed Sword", 55))

    # mordred ----

    mordred = Knight("Mordred", power=30, hp=90)
    mordred.equip_armour(Armour("breastplate", 15))
    mordred.equip_armour(Armour("boots", 10))
    mordred.equip_weapon(Weapon("Poisoned Sword", 60))
    mordred.drink_potion(Potion("Berserk", {
        "power": +15,
        "hp": -5,
        "protection": +10
    }))

    # red_knight ----

    red_knight = Knight("Red Knight", power=40, hp=70)
    red_knight.equip_armour(Armour("breastplate", 25))
    red_knight.equip_weapon(Weapon("Sword", 45))
    red_knight.drink_potion(Potion("Blessing", {"hp": +10, "power": +5}))

    # BATTLE:

    # 1 Lancelot vs Mordred:

    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:

    fight(arthur, red_knight)

    # Return battle results:

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle())
