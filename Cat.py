# This file defines the behavior of Cat.

from Turtle import Turtle
from Vector import *
from Color import *
from math import pi, sqrt
from Mouse import METER

class Cat(Turtle):

    def __init__(self, position, heading, speed, mouse, fill=blue,  **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.speed = speed
        self.catch = False
        self.mouse=mouse
        self.state=0


    def getnextstate(self):

        last_heading = self.heading
        distance = sqrt((self.position.x - 200)**2 + (self.position.y - 200)**2)

        in_base=(distance <= 30.1)

        if distance * cos(atan2(self.position.x - 200, 200 - self.position.y) - atan2(self.mouse.position.x - 200, 200 - self.mouse.position.y)) >= 1.0:
            self.state = 1

        if self.catch :
            self.heading, self.speed = 0, 0
            self.state = 0

        elif in_base:
            self.heading = atan2(200 - self.position.x, self.position.y - 200) * 180 / pi + 90 - (1.25 * METER / distance * 180 / pi) / 2
            self.speed = 2 * distance * sin(1.25 * METER / 2 / distance)
            self.state = 0

        elif self.state == 1:
            self.heading = atan2(200 - self.position.x, self.position.y - 200) * 180 / pi
            self.speed = METER

        elif self.state == 0:

            self.heading=atan2(200 - self.position.x, self.position.y - 200) * 180 / pi+90 - (1.25 * METER / distance * 180 / pi) / 2
            self.speed = 2 * distance * sin(1.25 * METER / 2 / distance)


        if sqrt((self.position.x - 200)**2 + (self.position.y - 200)**2) <= 30.1 \
                and (cos(self.mouse.heading * pi / 180 - last_heading * pi / 180) > cos(self.heading * pi / 180 - last_heading * pi / 180)) \
                and (cos(self.heading * pi / 180 - self.mouse.heading * pi / 180) > cos(self.heading * pi / 180 - last_heading * pi / 180)):
            self.catch = True
            self.mouse.set_catched(True)
            print "The mouse was Catched"

        if self.state==0:
            return self.position + unit(self.heading) * self.speed, self.heading
        elif distance >= 2 * METER:
            return self.position + unit(self.heading) * self.speed, self.heading
        else:
            return Vector(200 - METER * sin(atan2(200 - self.position.x, self.position.y - 200)), 200 + METER * cos(atan2(200 - self.position.x, self.position.y - 200))), self.heading
