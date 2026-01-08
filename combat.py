from Enemies import mob 
from playerClasses import character
import random as rand
moves = [
    {
        "name":"Bite",
        "dmg":20,
        "accuracy":1,
        "type":"undead"
        "heal":10,
    },
        {
        "name":"Basic Sword",
        "dmg":30,
        "accuracy":1,
        "type":"normal",
        "heal": None
    },
]
class battleStuff:
    def noNeg(num):
        if num < 0:
            return 0
        return num
    def heal(who,move,mobOrPlayer):
        if move is not None:
            if mobOrPlayer == "mob":
                
    def playerAttack(playerMoves,playerStats,enemieStats,enemie):
        for i in range(len(playerMoves)):
            print(f"{i+1}: {playerMoves[i]}")
        chosenMove = int(input("Chose a move!(A number here pls dont break my code i'll fix this later) "))
        chosenMove = playerMoves[chosenMove - 1]
        for i in range(len(moves)):
            if moves[i]["name"] == chosenMove:
                move = moves[i]
        chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
        dmg = round(move["dmg"] * playerStats["attack"]/enemieStats["defense"],1)
        if rand.randint(1,100) < chanceToHit:
            print(f"You used {move["name"]}!")
            enemie.doDamage(dmg)
            print(f"{enemie.returnName()} is at {battleStuff.noNeg(enemie.returnHP())} HP")
        return enemie
    def enemieAttack(enemieMoves,playerStats,enemieStats,player):
        chosenMove = rand.choice(enemieMoves)
        for i in range(len(moves)):
            if moves[i]["name"] == chosenMove:
                move = moves[i]
        chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
        dmg = round(move["dmg"] * enemieStats["attack"]/playerStats["defense"],1)
        if rand.randint(1,100) < chanceToHit:
            print(f"You were attacked with {move["name"]}")
            player.doDmg(dmg)
            print(f"You are at {battleStuff.noNeg(player.returnHP())} HP")
        return player
    def battle(enemie,player):
        enemieStats = enemie.returnStats()
        playerStats = player.returnStats()
        enemieMoves = enemie.returnMoves()
        playerMoves = player.returnMoves()
        battle = True
        print(f"You encountered {enemie.name}")
        while battle:
            if playerStats["speed"] > enemieStats["speed"]:
                enemie = battleStuff.playerAttack(playerMoves,playerStats,enemieStats,enemie)
                if enemie.Alive():
                    player = battleStuff.enemieAttack(enemieMoves, playerStats,enemieStats,player)
            elif playerStats["speed"] < enemieStats["speed"]:
                player = battleStuff.enemieAttack(enemieMoves, playerStats,enemieStats,player)
                if player.isAlive():
                    enemie = battleStuff.playerAttack(playerMoves,playerStats,enemieStats,enemie)
            if enemie.Alive() == False:
                battle = False
                loot = enemie.lootdrop()
                player.addToInventory(loot)
                print(f"You defeated {enemie.returnName()}!")
            elif player.isAlive() == False:
                battle = False
                print("YOU DIED!")
                quit()
        return player

player = character("player",100,50,50,100,50,1,[],[],["Basic Sword"])
enemie = mob(1,7,"zombie",20,20,20,25,1,["Iron","Rotten Flesh"],1,None,1,["Bite"])
player = battleStuff.battle(enemie,player)
