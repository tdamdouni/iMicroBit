# micro:owl - Displays the BBC Micro owl logo on a 
# BBC micro:bit and uses the accelerometer to scroll
# it around
#
# Copyright (c) 2016 John Graham-Cumming

from microbit import *

owl = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

# Height and width of the owl
h = len(owl)
w = len(owl[0])

# Location of the current 5x5 part of the owl being displayed
# (ox, oy) is the top left corner
ox = 0
oy = 0

# paint draws a 5x5 chunk of the owl on the micro:bit display
# starting from (ox, oy)
def paint():
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, 9 * owl[y+oy][x+ox])

# Defines how much the micro:bit has to be displaced for the
# acceleromoter to cause the owl to move
sensitivity = 100

paint()
while True:
    lastx = ox
    lasty = oy
    
    xa = accelerometer.get_x()
    if abs(xa) > sensitivity:
        if xa > 0 and ox > 0:
            ox -= 1
        elif xa < 0 and ox < w - 5:
            ox += 1

    ya = accelerometer.get_y()
    if abs(ya) > sensitivity:
        if ya > 0 and oy > 0:
            oy -= 1
        elif ya < 0 and oy < h - 5:
            oy += 1

    if lastx != ox or lasty != oy:
        paint()
        sleep(100)
