from playerClasses import player



class craftingfunc():
    def __init__(self):

        self.chosen_item_index = None
        self.item_used = []

        self.recipes =[
    
        {"item":"Iron Sword",
          "recipe":"Iron "*2},
        {"item":"Blood Wand", 
         "recipe":"Vampire_Essence " * 5},
        {"item":"Blood Sword", 
         "recipe":"Vampire_Essence, Vampire_Essence, Vampire_Essence, Vampire_Essence, Vampire_Essence, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"},
        {"item":"Iron Chestplate",
        "recipe":"Iron "*7},
        {"item":"Iron Leggings",
         "recipe":"Iron "*4
         },
         {"item":"Iron Boots",
          "recipe":"Iron "*3}

        ]

    def showalltheitemsandstuff(self):
        numberofitems = 1
        for things in self.recipes:
            print(f" {numberofitems}: {things["item"]}")
            print(f"RECIPE: {things["recipe"]}")
            print("--------------------")
            numberofitems +=1



    def inputmats(self):
        global player
        playerinvecopy = player["inventory"].copy()
        print("----------------------------------------------------------------------------------------")
        print("EXAMPLE: item: Iron, Vampire_Essence.")
        print("You would input Iron first, then Vampire_Essence, IT WILL NOT WORK THE OTHER WAY!!!! ")
        print("-----------------------------------------------------------------------------------------")
        while True:
            print(f" What you have right now: {playerinvecopy}")
            iteminput = input("Add items to craft(PUT WHAT YOU WANNA CRAFT IN ORDER!!!): ").title()
            
            if iteminput in playerinvecopy:
                playerinvecopy.remove(iteminput)
                self.item_used.append(iteminput)
            elif iteminput == "+":
                break
            else: 
                print(f" you dont have the item '{iteminput}'")


    def checkcraft(self, desired_item):
        for recipes, dic in enumerate(self.recipes):
            if dic["item"] == desired_item:
                self.chosen_item_index = recipes
            #if recipes["item"].title() == desired_item.title():
                #self.chosen_item_index = self.recipes.index(recipes["item"])

        if self.chosen_item_index == None:
            print("Not valid item")
        


    def craft_item(self):
        can_give_item = False
        if self.item_used == self.recipes[self.chosen_item_index]["recipe"].split():
            for item in self.item_used:
                if item in player_invetory:
                    player_invetory.remove(item)
                    can_give_item = True
        else:
            print("you cant  craft it not valid mats or wrong order")
        if can_give_item == True:
            player_invetory.append(self.recipes[self.chosen_item_index]["item"])
            print(f" You have crafted {self.recipes[self.chosen_item_index]["item"]}")
            
        
        
        playerinvecopy.clear()
        self.item_used.clear()
        print(player_invetory)
crafting = craftingfunc()
crafting.inputmats()
           

