from microbit import *
import random

dice = [4, 6, 8, 10, 12, 20]
die = 0


def maybe_update_die():
    global die
    if button_a.was_pressed():
        die = (die - 1) % len(dice)
        return True
    if button_b.was_pressed():
        die = (die + 1) % len(dice)
        return True
    return False


def display_die():
    display.scroll("D%s" % dice[die], loop=True, wait=False)


def roll_die():
    display.clear()
    sleep(500)
    display.show([Image.HEART,
                  str(random.randint(1, dice[die])),
                  Image.HEART],
                 delay=1000, loop=False, wait=True)


display_die()

while True:
    if maybe_update_die():
        display_die()

    if accelerometer.was_gesture('shake'):
        roll_die()
        display_die()
