# Copyright (C) 2016 Antonio Niño Díaz
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from microbit import *
import neopixel
from random import randint


ROWS = 4
COLUMNS = 8


# Setup the Neopixel strip on pin0 with a length of 4 pixels
np = neopixel.NeoPixel(pin0, 32)


class System:

    class Particle:
        x = 0
        y = 0
        r = 0
        g = 0
        b = 0

    NUMBER_OF_PARTICLES = 1
    particles = []

    def start(self, num):
        self.particles = []

        if num < 1:
            self.NUMBER_OF_PARTICLES = 1
        elif num > ROWS*COLUMNS:
            self.NUMBER_OF_PARTICLES = ROWS*COLUMNS
        else:
            self.NUMBER_OF_PARTICLES = num

        for i in range(self.NUMBER_OF_PARTICLES):
            p = self.Particle()
            p.x = i % COLUMNS
            p.y = i / COLUMNS
            p.r = randint(1, 4) * 8
            p.g = randint(1, 4) * 8
            p.b = randint(1, 4) * 8
            self.particles.append(p)

    # 31 ... 24
    # 23 ... 16
    # 15 ...  8
    #  7 ...  0

    def draw(self):
        for pixel_id in range(32):
            np[pixel_id] = (0, 0, 0)
        for p in self.particles:
            pixel_id = int(p.x) + int(p.y) * COLUMNS
            np[pixel_id] = (p.r, p.g, p.b)
        np.show()

    def check_empty(self, xx, yy):
        if int(yy) > ROWS-1 or int(yy) < 0 or int(xx) > COLUMNS-1 or int(xx) < 0:
            return False
        for p in self.particles:
            if int(p.x) == int(xx) and int(p.y) == int(yy):
                return False
        return True

    def update(self, ax, ay):
        for p in self.particles:
            if ay < -1024/4:
                if self.check_empty(p.x, p.y + 1):
                    p.y = p.y + 1
            elif ay > 1024/4:
                if self.check_empty(p.x, p.y - 1):
                    p.y = p.y - 1

            if ax < -1024/4:
                if self.check_empty(p.x - 1, p.y):
                    p.x = p.x - 1
            elif ax > 1024/4:
                if self.check_empty(p.x + 1, p.y):
                    p.x = p.x + 1

# Main function
# -------------

nump = ROWS*COLUMNS*6/11
s = System()
s.start(nump)

while True:
    if button_a.is_pressed() and nump < ROWS*COLUMNS-1:
        while button_a.is_pressed():  # Wait until released
            sleep(100)
        nump = nump + 1
        s.start(nump)
    if button_b.is_pressed() and nump > 1:
        while button_b.is_pressed():  # Wait until released
            sleep(100)
        nump = nump - 1
        s.start(nump)

    x = accelerometer.get_x()
    y = accelerometer.get_y()
    s.update(x, y)
    s.draw()
#   sleep(10)
