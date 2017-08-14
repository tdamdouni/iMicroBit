"""Compass: guess the heading.

Rotate the micro:bit to try finding the random heading that was picked by the
micro:pit. The closer you are from the answer, the brighter the screen will be.
"""
from microbit import *
from random import randint
from utils import blink


FULL = Image().invert()  # Maximum brightness for all pixels.


if not compass.is_calibrated():
    compass.calibrate()


def angle_diff(a, b):
    """Return the absolute difference between two angles."""
    abs_diff = abs(a - b) % 360
    diff = abs_diff if abs_diff < 180 else 360 - abs_diff
    return diff


while True:
    target = randint(0, 360)
    while True:
        heading = compass.heading()
        diff = angle_diff(heading, target)
        if diff < 5:
            blink(FULL)
            break
        else:
            # Bigger the difference, lower the ratio, lower the brightness.
            ratio = (100 - (diff * 100 / 360)) / 100
            display.show(FULL * ratio)
