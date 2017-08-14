""" This program needs a buzzer that will make a sound if there is current going through it. 
I placed the buzzer on the breadboard straddling the middle divide.  
The longer leg was connected via a jumper wire to pin1. The other leg was connected to the ground.
Pin 1 will be an output pin, and when it is set on, the buzzer will sound."""

from microbit import *

while True:
    if button_a.is_pressed():
        pin1.write_digital(1)
        display.show(Image.YES)
    if button_b.is_pressed():
        pin1.write_digital(0)
        display.show(Image.NO)