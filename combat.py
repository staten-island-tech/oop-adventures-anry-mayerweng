from Enemies import mob 
from playerClasses import character
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
    enemie