import math
import random

class Dice:
    def __init__(self):
        self.n = random.randint(1, 6)

    def bro(self):
        self.n = random.randint(1, 6)

    

class Gamer:

    def __init__(self, name, n = 0):
        self.name = name
        
##    def brosok(self):
##        dice = Dice()
##        self.n = dice.n
##        return self.n

    def brosok(self, dice):
        dice.bro()
        self.n = dice.n
        return self.n

    def __str__(self):
        return "У игрока {0.name!r} выпало {0.n!r} очков".format(self)


g1 = Gamer('Vds')
##g1.brosok()
##print(g1)
##g1.brosok()
##print(g1)

d1 = Dice();
print(d1.n)
g1.brosok(d1)
print(g1)
g1.brosok(d1)
print(g1)
