# Press button A for a fortune cookie.
from microbit import *
import random


fortunes = [
    "Never step off a moving bus",
    "This sentence is false",
    "The meaning of life is overrated",
    "Do not touch!",
    "You will receive some advice",
    "My hovercraft is full of eels",
    ]


while True:
    if button_a.is_pressed():
        cookie = random.choice(fortunes)
        display.scroll(cookie)
