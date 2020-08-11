class Things:
    pass

class Animate (Things):
    pass

class Animals(Animate):
    def breathe(self):
        pass

    def move(self):
        pass

    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_young_with_milk(self):
        pass

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass


reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()

     



