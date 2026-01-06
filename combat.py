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
        "name":"Basic Sword",
        "dmg":30,
        "accuracy":1,
        "type":"normal"
    },
]
def playerAttack(playerMoves,playerStats,enemieStats,enemie):
    for i in range(len(playerMoves)):
        print(f"{i+1}: {playerMoves[i]}")
    chosenMove = int(input("Chose a move!(A number pls dont break my code ill fix this later) "))
    chosenMove = playerMoves[chosenMove - 1]
    for i in range(len(moves)):
        if moves[i]["name"] == chosenMove:
            move = moves[i]
    chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
    dmg = move["dmg"] * playerStats["attack"]/enemieStats["defense"]
    if rand.randint(1,100) < chanceToHit:
        enemie.doDamage(dmg)
    return enemie
def enemieAttack(enemieMoves,playerStats,enemieStats,player):
    chosenMove = rand.choice(enemieMoves)
    for i in range(len(moves)):
        if moves[i]["name"] == chosenMove:
            move = moves[i]
    chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
    dmg = move["dmg"] * enemieStats["attack"]/playerStats["defense"]
    if rand.randint(1,100) < chanceToHit:
        player.doDmg(dmg)
    return player
def battle(enemie,player):
    enemieStats = enemie.returnStats()
    playerStats = player.returnStats()
    enemieMoves = enemie.returnMoves()
    playerMoves = player.returnMoves()
    battle = True
    while battle:
        if playerStats["speed"] > enemieStats["speed"]:
            enemie = playerAttack(playerMoves,playerStats,enemieStats,enemie)
            if enemie.Alive():
                player = enemieAttack(enemieMoves, playerStats,enemieStats,player)
        elif playerStats["speed"] < enemieStats["speed"]:
            player = enemieAttack(enemieMoves, playerStats,enemieStats,player)
            if player.isAlive():
                enemie = playerAttack(playerMoves,playerStats,enemieStats,enemie)
        if not enemie.Alive():
            battle = False
            loot = enemie.lootdrop()
            player.addToInventory(loot)
        elif not player.isAlive():
            battle = False
            print("YOU DIED")
            quit()
    return player

player = character("your mother",100,50,50,100,50,1,[],[],["Basic Sword"])
enemie = mob(1,7,"your uncle",50,50,50,25,1,[],1,None,1,["Bite"])
player = battle(enemie,player)
