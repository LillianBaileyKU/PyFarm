from farm import Farm

class Shop:
    def __init__(self):
        self.buy_prices = {
            "Wheat Seed":30,
            "Corn Seed":50,
            "Soybean Seed":25,
            "Tomato Seed":35,
            "Potato Seed":40,
            "Hay Seed":40,
            "Cow":150,
            "Chicken":100,
            "Sheep":250,
            "Field Upgrade":500,
            "Barn Upgrade":1000
            }

        self.sell_prices = {
            "Wheat":120,
            "Corn":150,
            "Soybean":50,
            "Tomato":80,
            "Potato":100,
            "Milk":85,
            "Egg":55,
            "Wool":105
        }

        self.animalproducts = {
            "Cow":"Milk",
            "Chicken":"Egg",
            "Sheep":"Wool"
        }

    def buy_item(self, farm, item):
        if item in self.buy_prices.keys():
            if item == "Cow" or item == "Chicken" or item == "Sheep" or item == "Field Upgrade" or item == "Barn Upgrade":
                print("Error buying item, please try again!")
                return
            if farm.remove_money(self.buy_prices[item]):
                farm.inventory.add_item(item, 1)
            else:
                print("You don't have enough money for that!")

    def buy_animal(self, farm, animal):
        if farm.barn.find_empty_stall():
            if animal in self.buy_prices.keys():
                if farm.remove_money(self.buy_prices[animal]):
                    farm.barn.add_animal(animal, self.animalproducts[animal], 0)
                else:
                    print("You don't have enough money for that!")
        else:
            print("Your barn is full!")

    def sell_item(self, farm, item):
        if item in self.sell_prices.keys():
            if not farm.inventory.has_item(item, 1):
                print(f"You don't have any {item}!")
            else:
                farm.add_money(self.sell_prices[item] * farm.inventory.get_amount(item))
                farm.inventory.remove_item(item, farm.inventory.get_amount(item))

    def buy_field_upgrade(self, farm):
        if farm.field.level >= 6:
            print("Your farm is already max level!")
        else:
            if farm.remove_money(self.buy_prices["Field Upgrade"]):
                farm.field.upgrade()
                self.buy_prices["Field Upgrade"] = int(self.buy_prices["Field Upgrade"] * 1.5)
            else:
                print("You don't have enough money for that!")

    def buy_barn_upgrade(self, farm):
        if farm.barn.level >= 5:
            print("Your barn is already max level!")
        else:
            if farm.remove_money(self.buy_prices["Barn Upgrade"]):
                farm.barn.upgrade()
                self.buy_prices["Barn Upgrade"] = int(self.buy_prices["Barn Upgrade"] * 1.8)
            else:
                print("You don't have enough money for that!")

    def display_buy_menu(self):
        print("Item | Price")
        for item, price in self.buy_prices.items():
            print(f"{item} | {price}")

    def display_sell_menu(self, inventory):
        tosell = {}
        for item, amt in inventory.playerinv.items():
            if item in self.sell_prices.keys():
                tosell[item] = amt
        if len(tosell) == 0:
            print("You have nothing to sell!")
        else:
            print("Item (Amount) | Price")
            for item, amt in tosell.items():
                print(f"{item} ({amt}) | {self.sell_prices[item]}")