"""
Snowflakes are symmetrical, we should only have to create a 3x3 corner and rotate

End result might resemble a star-wars spaceship instead of snowball.
Equally seasonal imho...
"""
from microbit import *

SIDE_SIZE = 3

BRIGHTNESS = {
    0: 0,
    1: 4,
    2: 9,
}


def get_random_corner():
    return [[random(3) for _ in range(SIDE_SIZE)] for _ in range(SIDE_SIZE)]


def get_flake():
    flake = list(get_random_corner())

    for row in flake:
        row += reversed(row[:-1])  # Middle column doesn't change

    for row in reversed(flake[:-1]):
        flake.append(row)

    return flake


def to_display(flake):
    for y, row in enumerate(flake):
        for x, col in enumerate(row):
            display.set_pixel(x, y, BRIGHTNESS[col])


while True:
    flake = get_flake()
    to_display(flake)
    sleep(1000)
