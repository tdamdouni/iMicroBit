# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *

def dark_left():
    return not button_b.is_pressed()
    
def dark_right():
    return not button_a.is_pressed()

while True:
    if dark_left() and dark_right():
        display.show("B")
    elif dark_right():
        display.show("R")
    elif dark_left():
        display.show("L")
    else:
        display.show("N")
            
    
    