"""Micropython loader.

This will only work if you have flashed an "empty micropython runtime" hex file
(using the uflash utility).
The loader will display the first module that it found on the micro:bit
filesystem. To skip to the next one, use the A button. To run the current
module, press B.

If there's only one module present, it'll run it straight away, without having
to select it.
"""
import os
from microbit import *


files = os.listdir()
modules = [file_[:-3] for file_ in files
           if (file_ != 'main.py'
               and file_ != 'utils.py'
               and file_.endswith('.py'))]


while True:  # Outer loop: cycle between choices.
    if not modules:
        display.scroll(
            "Upload micropython modules to the micro:bit filesystem using the "
            "ufs utility",
            loop=True)
    if len(modules) == 1:  # Only one module? Run it straight away.
        __import__(modules[0])
    for module in sorted(modules):
        display.scroll(module, wait=False, loop=True)
        # Inner loop: keep scrolling current choice until a button is pressed.
        a_pressed = button_a.was_pressed()
        b_pressed = button_b.was_pressed()
        while not a_pressed and not b_pressed:
            a_pressed = button_a.was_pressed()
            b_pressed = button_b.was_pressed()

        if a_pressed:  # Skip this one, display the next choice.
            continue
        elif b_pressed:  # Run the current choice.
            __import__(module)
