
player_invetory =["Vampire Essence", "Vampire Essence", "Vampire Essence", "Vampire Essence", "Vampire Essence"]
crafting_recipes = [
    
        {"item":"Iron Sword",
          "recipe":"Iron "*2},
        {"item":"Blood Wand", 
         "recipe": "Vampire Essense "*5},
        {"item":"Blood Sword", 
         "recipe":"Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"}
        ]


class craftingfunc():
    def __init__(self):

        self.chosen_item_index = None
        self.item_used = []

        self.recipes =[
    
        {"item":"Iron Sword",
          "recipe":"Iron "*2},
        {"item":"Blood Wand", 
         "recipe":"Vampire Essence " * 5},
        {"item":"Blood Sword", 
         "recipe":"Vampire Essence, Vampire Essence, Vampire Essence, Vampire Essence, Vampire Essence, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"}
        ]


    def inputmats(self):
        global playerinvecopy
        playerinvecopy = player_invetory.copy()
        while True:
            iteminput = input("Add items to craft: ").title()
            if iteminput in playerinvecopy:
                playerinvecopy.remove(iteminput)
                self.item_used.append(iteminput)
            elif iteminput == "+":
                break
            else: 
                print(f" you dont have the item '{iteminput}'")
        print(self.item_used)


    def checkcraft(self, desired_item):
        for recipes, dic in enumerate(self.recipes):
            if dic["item"] == desired_item:
                self.chosen_item_index = recipes
            #if recipes["item"].title() == desired_item.title():
                #self.chosen_item_index = self.recipes.index(recipes["item"])

        if self.chosen_item_index == None:
            print("Not Real item bro")
        


    def craft_item(self):
        can_give_item = False
        if self.item_used.strip() == self.recipes[self.chosen_item_index]["recipe"].split().strip():
            for item in self.item_used:
                if item in player_invetory:
                    player_invetory.remove(item)
                    can_give_item = True
        else:
            print("you cant  craft it no valid mats")
        if can_give_item == True:
            player_invetory.append(self.recipes[self.chosen_item_index]["item"])
        
        
        playerinvecopy.clear()
        self.item_used.clear()
        print(player_invetory)
        print(self.recipes[self.chosen_item_index]["recipe"].split())
               

crafting = craftingfunc()
crafting.inputmats()
crafting.checkcraft("Blood Wand")
crafting.craft_item()
           

