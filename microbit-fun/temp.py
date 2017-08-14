"""Temperature.

Nothing to do but to read the temperature measured by the micro:bit.
"""
from microbit import *
from utils import NUMBERS, image_from_number, zigzag


while True:
    temp = str(temperature())
    img = image_from_number(temp)
    def get_temp_to_display():
        return image_from_number(str(temperature()))
    zigzag(get_temp_to_display, 50, 300)
