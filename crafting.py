
player_invetory =["Iron", "Iron"]
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
         "recipe": "Vampire Essense "*5},
        {"item":"Blood Sword", 
         "recipe":"Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"}
        ]


    def inputmats(self):
        while True:
            iteminput = input("Add items to craft: ").title()
            if iteminput in player_invetory:
                playerinvecopy = player_invetory.copy()
                playerinvecopy.remove(iteminput)
                self.item_used.append(iteminput)
            elif iteminput == "+":
                break
            else: 
                print(f" you dont have the item '{iteminput}'")
        print(self.item_used)


    def checkcraft(self, desired_item):
        for recipes in self.recipes:
            if recipes["item"].title() == desired_item.title():
                self.chosen_item_index = recipes["item"].index(recipes["item"])

            if self.chosen_item_index == None:
                return
            
        print(self.chosen_item_index)


    def craft_item(self):
        for item in self.recipes[{self.chosen_item_index}]["recipe"]:
            print(item)

crafting = craftingfunc()
crafting.checkcraft("Iron Sword")
crafting.craft_item()
           

