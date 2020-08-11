class Things:
    pass

class Animate:
    pass

class Animals(Animate):  
    def breathe(self):
        print("breathing")        
    def move(self):
        print("moving")        

    def eat_food(self): 
        print("eat food")        

class Mammals(Animals):
    def feed_young_with_milk(self):            
        print("feed young")        


class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print("eat leaves from trees")        

reginald = Giraffes()
harold = Giraffes()
reginald.move()

harold.eat_leaves_from_trees()

import turtle
avery = turtle.Pen()
kate = turtle.Pen()

