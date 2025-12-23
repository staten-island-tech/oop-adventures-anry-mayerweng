import random as r


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

Vampire_names = ["Draven", "Lilith", "Lucien", "Nyx", "Vesper"]

Vampire_lootdrops = ["Vampire Essence",
                      "Silver helment", 
                      "Silver Leggings", 
                      "Silver Chestplate"]

Zombie_lootdrops = ["Flesh",
                     "Iron",
                     "Zombie Head", 
                     "Ripped Shirt"]

Skeleton_lootdrops = ["Bones",
                      "Chainmail "
                      "Skeleton head",
                      "Goggles"]


mob1 = [
    {
        "name": "Zombie",
        "hp":r.randint(50,70), 
        "attack":r.randint(4,7), 
        "mob_name": r.choice(zombie_names), 
        "lootdrops":r.choice(Zombie_lootdrops), 
        "speed":r.randint(1,2), 
        "defense":r.randint(2,6),
        "chance":r.randint(1,4),
        "debuff": None,
        "debuffmulti": 1
    },
    {
        "name": "Vampire",
        "hp":r.randint(60,100), 
        "attack":r.randint(3,6), 
        "mob_name": r.choice(Vampire_names), 
        "lootdrops":r.choice(Vampire_lootdrops), 
        "speed":r.randint(4,7), 
        "defense":r.randint(1,4),
        "chance":r.randint(1,6),
        "debuff": None,
        "debuffmulti": 1
    },
    {
    "name": "Skeleton",
        "hp":r.randint(30,50), 
        "attack":r.randint(5,9), 
        "mob_name": r.choice(skeleton_names), 
        "lootdrops":r.choice(Skeleton_lootdrops), 
        "speed":r.randint(2,3), 
        "defense":r.randint(1,4),
        "chance":r.randint(1,5),
        "debuff": None,
        "debuffmulti": 1
    }
]
        




invetory =[]



class mob():
    def __init__(self, levelmin,levelmax, mob_name ,health,attack,speed,defense,lootdrops,chance,debuff,debuffmulti,moves):
        self.level = r.randint(levelmin, levelmax)
        self.name = mob_name
        self.health = int(health * (self.level * .40))
        self.attack = attack + self.level
        self.speed = speed + self.level
        self.debuffmulti = debuffmulti
        self.defense = int(defense * self.level * self.debuffmulti)
        self.lootdrops = lootdrops
        self.chance = chance
        self.debuff = debuff
        self.moves = moves
    def lootdrop(self):
        chance = r.randint(1,chance)
        if chance == 1:
            loot = r.choice(self.lootdrops)
            return loot
    def Alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def Dodamage(self, attack):
        self.health -= attack



zombie = mob(1,5,
             r.choice(zombie_names)
             ,r.randint(50,70)
             ,r.randint(4,7)
             ,r.randint(3,6)
             ,r.randint(2,6)
             ,r.choice(Zombie_lootdrops),
             4,
             None,
             1,
             )

print(zombie.name)
zombie.lootdrop()
