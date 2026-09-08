from field import Field
from barn import Barn
from inventory import Inventory
from plot import Plot

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
        