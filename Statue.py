from Turtle import Turtle
from Vector import *
from Color import *

meter = 30

class Statue(Turtle):

    def __init__(self, position, heading, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)

    def getshape(self):
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward * 0.8 * meter,
                self.position - right * 0.8 * meter,
                self.position - forward * 0.8 * meter,
                self.position + right * 0.8 * meter]

    def getnextstate(self):
        return self.position, self.heading