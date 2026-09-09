from animal import Animal

class Barn:
    def __init__(self, animals, level):
        self.animals = animals
        self.level = level

    def get_animal(self, number):
        #Note: number expects controller to have already subtracted 1 to correctly index
        try:
            return self.animals[number]
        except:
            print("Not a valid stall!")

    def display_barn(self):
        for i in self.animals:
            i.display_status()
        
    def add_animal(self, animal, product, time):
        for count, i in enumerate(self.animals):
            if self.animals.type == None:
                self.animals[count] = Animal(animal, 0, product, time, False)
                return True
        return False

    def find_empty_stall(self):
        for stall in self.animals:
            if stall.type == None:
                return True
        return False

    def upgrade(self):
        for i in range(2):
            self.animals.append(Animal(None, 0, None, 0, False))
        self.level += 1
