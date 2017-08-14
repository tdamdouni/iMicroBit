from microbit import *
import random

dice_faces = [
    Image('00000:00000:00000:00000:00000'),
    Image('00000:00000:00900:00000:00000'),
    Image('00000:09000:00000:00090:00000'),
    Image('00000:09000:00900:00090:00000'),
    Image('00000:09090:00000:09090:00000'),
    Image('00000:09090:00900:09090:00000'),
    Image('00000:09090:09090:09090:00000')
]

value = 0
rolling = False

while True:
    if button_a.was_pressed():
        rolling = not rolling
    if button_b.was_pressed():
        rolling = False
        value = 0
    if rolling:
        value = random.randint(1, 6)
    display.show(dice_faces[value])
    sleep(42)