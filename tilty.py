from microbit import *

TILT = 150


def centered(n):
    return -TILT < n < TILT


def pos_tilt(n):
    return TILT <= n


def neg_tilt(n):
    return n <= -TILT


while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if centered(x):
        if centered(y):
            display.show(Image.DIAMOND_SMALL)
        elif pos_tilt(y):
            display.show(Image.ARROW_N)
        elif neg_tilt(y):
            display.show(Image.ARROW_S)
    elif pos_tilt(x):
        if centered(y):
            display.show(Image.ARROW_W)
        elif pos_tilt(y):
            display.show(Image.ARROW_NW)
        elif neg_tilt(y):
            display.show(Image.ARROW_SW)
    else:
        if centered(y):
            display.show(Image.ARROW_E)
        elif pos_tilt(y):
            display.show(Image.ARROW_NE)
        elif neg_tilt(y):
            display.show(Image.ARROW_SE)
    sleep(100)
