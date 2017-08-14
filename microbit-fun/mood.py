"""Mood feedback.

Pressing the right button will display an increasingly bright happy face, until
it flashes to ack your mood.
Pressing the left button will instead display a sad face, and pressing both
buttons at once will display a "meh" face.
"""

from microbit import *
from utils import blink


def increase_while_pressed(buttons, img):
    """Increase the brightness of the image while buttons are pressed.

    If the brightness reaches its maximum, return True. If the buttons
    are released before, return False.
    """
    brightness = 0.1
    step = 0.001  # Don't increase too fast.
    while all([button.is_pressed() for button in buttons]):
        brightness += step
        display.show(img * brightness)
        if brightness >= 1:
            return True
    return False

while True:
    sleep(200)  # Need some time to detect a double button press.
    buttons = []
    img = None
    if button_a.is_pressed() and button_b.is_pressed():
        buttons = [button_a, button_b]
        img = Image.MEH
    elif button_a.is_pressed():
        buttons = [button_a]
        img = Image.SAD
    elif button_b.is_pressed():
        buttons = [button_b]
        img = Image.HAPPY
    if buttons and img:
        if increase_while_pressed(buttons, img):
            blink(img)  # User feedback: choice confirmed.
    display.clear()
