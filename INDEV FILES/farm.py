from field import Field
from barn import Barn
from inventory import Inventory

class Farm:
    def __init__(self, name, money, days, years, seasonday, seasonindex, inventory, field, barn, bankrupt, totalmoney, cropsharvested):
        self.name = name
        self.money = money
        self.days = days
        self.years = years
        self.season_day = seasonday
        self.season_index = seasonindex
        self.inventory = inventory
        self.field = field
        self.barn = barn
        self.bankrupt = bankrupt
        self.total_money = totalmoney
        self.crops_harvested = cropsharvested
        self.seasonlen = 15
        self.seasons = ["Spring", "Summer", "Fall", "Winter"]

    def display_status(self):
        print(f"You stand in the middle of {self.name} farm.")
        print(f"It is Year {self.years}, Season {self.seasons[self.season_index]}, Day {self.season_day}.")
        print(f"You have {self.money} in your wallet.")

    def add_money(self, amount):
        self.money += amount
        self.total_money += amount
    
    def remove_money(self ,amount):
        if self.money - amount >= 0:
            self.money -= amount
            return True
        else:
            return False
        
    def advance_day(self):
        self.days += 1
        self.season_day += 1
        if self.season_day > self.seasonlen:
            self.season_day = 1
            self.season_index = (self.season_index + 1) % len(self.seasons)
            if self.season_index == 0:
                self.years += 1
    
    def check_bankruptcy(self):
        if self.money <= 0:
            self.bankrupt = True
            return True
        else:
            return False