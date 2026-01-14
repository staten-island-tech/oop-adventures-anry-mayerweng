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




listofwordsnotinGear = ["leggings", "Chestplate", "Boots", "Mask"]
listofwordsnotinarmor = ["Sword", "Wand", "Dagger"]





print(pf.player.inventory)


class Armor:
    def __init__(self, maxhp, defense):
        self.maxhp = maxhp
        self.defense = defense
        self.playerset = []
    def remove_armor(self, theitemtoremove):
        if theitemtoremove in self.playerset:
            self.playerset.remove(theitemtoremove)
        else:
            print("you aint got that on")

    def add_armor(self, theitemtoadd):
        self.canaddarmor = True
        if theitemtoadd not in pf.player.inventory or len(self.playerset) == 4 or theitemtoadd in listofwordsnotinarmor:
            self.canaddarmor = False

        if self.canaddarmor == True:
            for stats in stats_armors:
                if stats["item"].lower() == theitemtoadd.lower():
                    pf.player.maxHP += stats["statsHP"]
                    pf.player.defense += stats["statsDEF"]
            print(pf.player.maxHP)
            print(pf.player.defense)
            
                    
        
            
class Gear:
    def __init__(self, attack, speed):
        self.attack = attack
        self.speed = speed



pf.player.inventory.append("Iron Chestplate")
player = Armor(pf.player.maxHP, pf.player.defense)
player.add_armor("Iron Chestplate")