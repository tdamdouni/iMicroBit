from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        display.show(str(random.randint(1, 6)))
    
display.clear()