from plot import Plot

class Field:
    def __init__(self, plots, level):
        self.plots = plots
        self.level = level

    def get_plot(self, number):
        #Note: number expects controller to have already subtracted 1 to correctly index
        try:
            return self.plots[number]
        except:
            print("Not a valid plot!")

    def display_field(self):
        for i in self.plots:
            i.display_status()

    def upgrade(self):
        for i in range(4):
            self.plots.append(Plot(len(self.plots) + 1, None, 0, None))
        self.level += 1
