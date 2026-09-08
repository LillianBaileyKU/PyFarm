class Inventory:
    def __init__(self, inv):
        #Inventory is expected to be passed as a dictionary
        self.playerinv = inv

    def add_item(self, item, amount):
        #Add new item to inventory
        if item in self.playerinv:
            self.playerinv[item] += amount
        else:
            self.playerinv[item] = amount

    def remove_item(self, item, amount):
        #Remove an item from inventory
        if item in self.playerinv:
            if self.playerinv[item] - amount <= 0:
                del self.playerinv[item]
            else:
                self.playerinv[item] -= amount
        else:
            pass

    def has_item(self, item, amount):
        #Return if the player has a specific item in a specific amount
        if item in self.playerinv and self.playerinv[item] >= amount:
            return True
        else:
            return False

    def get_amount(self, item):
        #Return how many items of a specific type the inventory has
        if item in self.playerinv:
            return self.playerinv[item]
        else:
            return 0

    def display_inventory(self):
        #Display the player's inventory
        print("Item | Amount")
        for item, count in self.playerinv.items():
            print(f"{item} | {count}")

