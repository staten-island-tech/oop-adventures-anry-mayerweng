import playerClasses as pf

stats_armors = [
    {"item":"Vampire Mask",
    "statsHP":70,
    "statsDEF":5},
     {"item":"Iron Chestplate",
    "statsHP":30,
    "statsDEF":30},
     {"item":"Iron Leggings",
    "statsHP":15,
    "statsDEF":30},
     {"item":"Iron Boots",
    "statsHP":10,
    "statsDEF":20},
]

stats_Gears_and_stuff = [
    {"item":"Blood Sword",
     "statsATK":20,
     "statsSPD":2},
     {"item":"Blood Wand",
     "statsATK":10,
     "statsSPD":1},
     {"item":"Blood Sword",
     "statsATK":12,
     "statsSPD":5},
]








chosenClass = pf.chosenClass
chosenData = pf.chosenData
player = pf.player


class Armor:
    def __init__(self, hp, defense):
        self.hp = hp
        self.defense = defense


class Gear:
    def __init__(self, attack, speed):
        self.attack = attack
        self.speed = speed

