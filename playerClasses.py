
class character:
    def __init__(self,name,HP,speed,attack,defense,evasiveness,inventory,equipped,moves):
        self.HP = HP
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
classNames = []
for i in range(len(classesjson)):
    classNames.append(classesjson[i]["name"])

name = input("What is your name?")
chosenClass = input(f"What class are you?{classNames}")
for i in range(len(classesjson)):
    for i in range*(len(classesjson)):
        if classesjson[i]["name"] == chosenClass:
            chosenData = classesjson[i]
            player = character(name,chosenData["HP"],chosenData["speed"],chosenData["attack"],chosenData["defense"],chosenData["evasiveness"],chosenData["inventory"],chosenData["moves"])



    