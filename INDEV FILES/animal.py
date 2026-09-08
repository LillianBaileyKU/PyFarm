class Animal:
    def __init__(self, type, production, product, producttime, fed):
        self.type = type
        self.production = production
        self.product = product
        self.producttime = producttime
        self.fed = fed

    def feed(self):
        if self.fed == True:
            print("That animal is already fed!")
            return False
        else:
            print(f"You fed your {self.type}!")
            self.fed = True
            return True

    def produce(self, amount):
        if self.fed and self.production < self.producttime:
            if self.production + amount <= self.producttime:
                self.production += amount
                self.fed = False
            else:
                self.production = self.producttime
                self.fed = False


    def is_ready(self):
        if self.production >= self.producttime:
            return True
        else:
            return False

    def collect(self):
        if self.is_ready():
            returnproduct = self.product
            self.production = 0
            return returnproduct

    def display_status(self):
        print(f"This stall contains a {self.type}!")
        print(f"It is at production stage {self.production}!")
        if self.fed:
            print(f"The {self.type} is fed!")
        else:
            print(f"The {self.type} is not fed!")