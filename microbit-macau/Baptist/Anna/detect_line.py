# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *

def left_is_dark():
    return not button_b.is_pressed()
    
    
def right_is_dark():
    return not button_a.is_pressed()


while True:
    if left_is_dark() and right_is_dark():
        display.show("B")
    elif right_is_dark():
        display.show("R")
    elif left_is_dark():
        display.show("L")
    else:
        display.show("N")
    
    
    
    
    
    