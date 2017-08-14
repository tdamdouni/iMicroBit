"""Pouring rain.

Or at least, something resembling pouring rain. Nothing to do, just watch (and
enjoy. Maybe).
"""
from microbit import *
import random


def set_first_line(img, pixels):
    """Set the first line of an image with the given pixel values."""
    for index, pixel in enumerate(pixels):
        img.set_pixel(index, 0, pixel)
    return img


img = Image()  # Start with an empty screen.
while True:
    img = img.shift_down(1)
    # New line of random ints: random pixels with random brightness.
    line = [random.randint(0, 9) for i in range(5)]
    img = set_first_line(img, line)
    display.show(img)
    sleep(100)
