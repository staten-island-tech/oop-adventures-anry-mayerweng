# import json
# data = open("./classes.json",encoding="utf8")
# classes = json.load(data)
classes = [   
        {
        "name":"Melee",
        "HP":80,
        "maxHP":80,
        "speed":80,
        "attack":120,
        "defense":80,
        "evasiveness":0.99,
        "inventory": [],
        "equipped": ["Basic Sword"],
        "moves": ["Sword Slash"]
    },
        {
        "name":"Tank",
        "HP":120,
        "maxHP":120,
        "speed":60,
        "attack":100,
        "defense":120,
        "evasiveness":1,
        "inventory": [],
        "equipped": ["Giant Fists","Basic Armor"],
        "moves": ["Giant Punch"]
    },
        {
        "name":"Assasin",
        "HP":60,
        "maxHP":60,
        "speed":120,
        "attack":110,
        "defense":60,
        "evasiveness":0.85,
        "inventory": [],
        "equipped": ["Basic Dagger"],
        "moves": ["Stab"]
    }
]
class character:
    def __init__(self,name,HP,maxHP,speed,attack,defense,evasiveness,inventory,equipped,moves):
        self.HP = HP
        self.maxHP = maxHP
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.evasiveness = evasiveness
        self.inventory = inventory
        self.equippted = equipped
        self.moves = moves
        self.name = name
    def returnStats(self):
        stats = {
            "attack":self.attack,
            "defense":self.defense,
            "speed":self.speed,
            "evasiveness": self.evasiveness
        }
        return stats
    def returnInventory(self):
        return self.inventory
    def returnEquipped(self):
        return self.equippted
    def addToInventory(self,item):
        self.inventory.append(item)
    def doDmg(self,dmg):
        self.HP = self.HP - dmg
    def heal(self,heal):
        self.HP = self.HP + heal
        if self.HP > self.maxHP:
            self.HP = self.maxHP
    def isAlive(self):
        if self.HP > 0:
            return True
        else:
            return False
classNames = []
for i in range(len(classes)):
    classNames.append(classes[i]["name"])

name = input("What is your name?")
chosenClass = input(f"What class are you?{classNames} ")
for I in range(len(classes)):
    for i in range(len(classes)):
        if classes[i]["name"] == chosenClass:
            chosenData = classes[i]
            player = character(name,chosenData["HP"],chosenData["speed"],chosenData["attack"],chosenData["defense"],chosenData["evasiveness"],chosenData["inventory"],chosenData["equipped"],chosenData["moves"])

