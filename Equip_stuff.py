from playerClasses import classes

print(classes[0])

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
