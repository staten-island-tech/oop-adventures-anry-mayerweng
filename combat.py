from Enemies import mob 
from playerClasses import character
import random as rand
moves = [
    {
        "name":"Bite",
        "dmg":20,
        "accuracy":1,
        "type":"undead",
        "heal":10,
        "attackChangeS":None,
        "attackChangeE":None,
        "defenseChangeS":None,
        "defenseChangeE":None,
        "speedChangeS":None,
        "speedChangeE":None
    },
        {
        "name":"Basic Sword",
        "dmg":30,
        "accuracy":1,
        "type":"normal",
        "heal": None,
        "attackChangeS":None,
        "attackChangeE":None,
        "defenseChangeS":None,
        "defenseChangeE":None,
        "speedChangeS":None,
        "speedChangeE":None
    }
]
class battleStuff:
    def noNeg(num):
        if num < 0:
            return 0
        return num
    def heal(who,move):
        if move["heal"] is not None:
            who.heal(move["heal"])
            print(f"{who.name} healed!")
        return who
    def atkChange(who,move,selfOrEnemie):
        if move["attackChange"+ selfOrEnemie] is not None:
            who.attack = who.attack * move["attackChange"+ selfOrEnemie]
            if selfOrEnemie == "S":
                word = "increased"
            else:
                word = "decreased"
            print(f"{who.name}'s attack {word}")
            
        return who
    def defChange(who,move,selfOrEnemie):
        if move["defenseChange"+ selfOrEnemie] is not None:
            who.attack = who.attack * move["defenseChange"+ selfOrEnemie]
            if selfOrEnemie == "S":
                word = "increased"
            else:
                word = "decreased"
            print(f"{who.name}'s attack {word}")
        return who
    def speedChange(who,move,selfOrEnemie):
        if move["speedChange"+ selfOrEnemie] is not None:
            who.attack = who.attack * move["speedChange"+ selfOrEnemie]
            if selfOrEnemie == "S":
                word = "increased"
            else:
                word = "decreased"
            print(f"{who.name}'s attack {word}")
        return who
    def statsChange(who,move,selfOrEnemie):
        who = battleStuff.atkChange(who,move,selfOrEnemie)
        who = battleStuff.defChange(who,move,selfOrEnemie)
        who = battleStuff.speedChange(who,move,selfOrEnemie)
        return who
    def playerAttack(playerMoves,playerStats,enemieStats,enemie,player):
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
            player = battleStuff.heal(player,move)
            player = battleStuff.statsChange(player,move,"S")
            enemie = battleStuff.statsChange(enemie,move,"E")
            print(f"{enemie.returnName()} is at {battleStuff.noNeg(enemie.returnHP())} HP")
        return enemie
    def enemieAttack(enemieMoves,playerStats,enemieStats,player,enemie):
        chosenMove = rand.choice(enemieMoves)
        for i in range(len(moves)):
            if moves[i]["name"] == chosenMove:
                move = moves[i]
        chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
        dmg = round(move["dmg"] * enemieStats["attack"]/playerStats["defense"],1)
        if rand.randint(1,100) < chanceToHit:
            print(f"You were attacked with {move["name"]}")
            player.doDmg(dmg)
            enemie = battleStuff.heal(enemie,move)
            enemie = battleStuff.statsChange(enemie,move,"S")
            player = battleStuff.statsChange(player,move,"E")
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
                enemie = battleStuff.playerAttack(playerMoves,playerStats,enemieStats,enemie,player)
                if enemie.Alive():
                    player = battleStuff.enemieAttack(enemieMoves, playerStats,enemieStats,player,enemie)
            elif playerStats["speed"] < enemieStats["speed"]:
                player = battleStuff.enemieAttack(enemieMoves, playerStats,enemieStats,player,enemie)
                if player.isAlive():
                    enemie = battleStuff.playerAttack(playerMoves,playerStats,enemieStats,enemie,player)
            if enemie.Alive() == False:
                battle = False
                loot = enemie.lootdrop()
                player.addToInventory(loot)
                print(f"You defeated {enemie.returnName()}!")
                print(f"You collected {loot}")
            elif player.isAlive() == False:
                battle = False
                print("YOU DIED!")
                quit()
        return player

player = character("player",100,50,50,100,50,1,[],[],["Basic Sword"])
enemie = mob(1,7,"zombie",20,20,20,25,1,["Iron","Rotten Flesh"],1,None,1,["Bite"])
player = battleStuff.battle(enemie,player)
