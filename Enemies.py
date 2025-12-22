import random

zombie_names = [
    "Shambling Corpse",
    "Rotwalker",
    "Graveborn",
    "Fleshdragger",
    "Mudclaw",
    "Hollow One",
    "Graveshuffler",
    "Rotting Husk",
    "Bonechewer",
    "Ashen Dead"
]

skeleton_names = [
    "Rattlebone",
    "Graveclatter",
    "Bonewalker",
    "Dustmarrow",
    "Crypt Rattler"
]


invetory =[]

class Undead:
    debuffactive = True
    if debuffactive == False:
        debuffmulti = 1
    else:
        debuffmulti = .8

class Zombie(Undead):
    def __init__(self,name):
        self.level = random.randint(1, 3)
        self.name = name
        self.health = int(100 * (self.level * .40))
        self.attack = 4 + self.level
        self.speed = self.level
        self.defense = int(3 * self.level * self.debuffmulti)

    def lootdrop(self):
        lootdrops = ["Flesh", "Iron","Zombie Head", "Ripped Shirt"]
        chance = random.randint(1,4)
        if chance == 1:
            loot = random.choice(lootdrops)
            return loot
    moves = ["Bite", "Stinky Breath"]

class Skeleton(Undead):
    def __init__(self,name):
        self.level = random.randint(1, 5)
        self.name = name
        self.health = int(60 * (self.level * .40))
        self.attack = 7 + self.level
        self.speed = self.level
        self.defense = int(1 * self.level * self.debuffmulti)

    def lootdrop(self):
        lootdrops = ["Bone", "Bow","Skeleton Head", "Chainmail Pants"]
        chance = random.randint(1,6)
        if chance == 1:
            loot = random.choice(lootdrops)
            return loot
    moves = ["Arrow Attack", "Long Shot"]

class Wither(Undead):
    def __init__(self,name):
            self.level = random.randint(5, 10)
            self.name = name
            self.health = int(150 * (self.level * .40))
            self.attack = 6 + self.level
            self.speed = self.level
            self.defense = int(7 * self.level * self.debuffmulti)

    def lootdrop(self):
        lootdrops = ["Wither Essence", "Iron helment", "Iron Leggings", "Iron Chestplate","Wither Artifact"]
        chance = random.randint(1,7)
        if chance == 1:
            loot = random.choice(lootdrops)
            return loot
    moves = ["Stab", "Blind Potion", "Screech"]






zombie = Zombie(random.choice(zombie_names))
skeleton = Skeleton(random.choice(skeleton_names))

print(zombie.name)
zombie.lootdrop()
