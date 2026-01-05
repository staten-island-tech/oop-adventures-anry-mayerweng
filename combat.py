from Enemies import mob 
from playerClasses import character
import random as rand
moves = [
    {
        "name":"Bite",
        "dmg":30,
        "accuracy":1,
        "type":"undead"
    },
        {
        "name":"Sword Slash",
        "dmg":30,
        "accuracy":1,
        "type":"normal"
    },
]
def battle(enemie,player):
    enemieStats = enemie.returnStats
    playerStats = player.returnStats
    enemieMoves = enemie.returnMoves
    playerMoves = player.returnMoves
    battle = True
    while battle:
        if playerStats["speed"] > enemieStats["speed"]:
            for i in range(len(playerMoves)):
                print(f"{i+1}: {playerMoves[i]}")
            chosenMove = int(input("Chose a move!"))
            chosenMove = playerMoves[chosenMove - 1]
            for i in range(len(moves)):
                if moves[i]["name"] == chosenMove:
                    move = moves[i]
            chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
            dmg = move["dmg"] * (playerStats[""])
            if rand.randint(1,100) < chanceToHit:
                enemie.doDamage()

        

