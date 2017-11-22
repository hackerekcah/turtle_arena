from Turtle import Turtle
from Vector import *
from Color import *
METER=30

class Mouse(Turtle):
    def __init__(self, position, heading, speed, fill=blue, stop=0, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.stop = stop
        self.catched = False

    def getnextstate(self):
        self.heading, self.speed = 0, 0
        if not self.catched:
            self.heading = atan2(200 - self.position.x, self.position.y - 200) * 180 / pi + 90 - (METER / 40.0 * 180 / pi) / 2.0
            self.speed = 2 * (METER + 10) * sin(3.0 / 8.0)
        return self.position + unit(self.heading) * self.speed, self.heading

    def getshape(self):
        forward = unit(self.heading)
        right = unit(self.heading + 90)

        return [self.position + forward * 5,
                self.position - right * 5,
                self.position + right * 5,
                self.position - forward * 5]

    def set_catched(self,catched):
        self.catched=catched


