class Plot:
    def __init__(self, number, crop, growth, growtime):
        self.number = number
        self.crop = crop
        self.growth = growth
        self.growtime = growtime

    def is_empty(self):
        #Check if the plot is empty
        if self.crop == None:
            return True
        else:
            return False

    def plant(self, crop, growtime):
        #Plant a crop
        if self.crop != None:
            return False
        else:
            self.crop = crop
            self.growth = 1
            self.growtime = growtime
            return True

    def grow(self, amount):
        #Grow a crop by a requested amount
        if self.crop != None:
            self.growth += amount

    def is_ready(self):
        #Check if a crop is ready to harvest
        if self.crop != None and self.growth >= self.growtime:
            return True
        else:
            return False

    def harvest(self):
        #Harvest the crop
        if self.is_ready():
            returncrop = self.crop
            self.crop = None
            self.growth = 0
            self.growtime = None
            return returncrop
        else:
            return False

    def display_status(self):
        #Display the status of the plot
        if self.crop == None:
            print(f"Plot {self.number} has nothing growing in it!")
        else:
            print(f"Plot {self.number} has {self.crop} growing in it! It is in growth stage {self.growth}!")