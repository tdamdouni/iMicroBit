# Add your Python code here. E.g.
from microbit import *
from bitbot import*
from neopixel import*

def left_is_dark():
    return not button_b.is_pressed()

def right_is_dark():
    return not button_a.is_pressed()

np=NeoPixel(pin13,12)

while True:
    for a in range(0,12):
            np[a]=(2,0,2)
    
    if left_is_dark() and right_is_dark():
        display.show("B")
        
        set_speed(-10,-10)
        for c in range(0,12):
            np[c]=(0,0,2)
    
    elif left_is_dark():
        display.show("L")
        set_speed(10,15)
        
        for a in range(0,6):
            np[a]=(3,2,10)
            
    elif right_is_dark():
        display.show("R")
        set_speed(15,10)
        for b in range(6,12):
            np[b]=(2,0,0)
            
            
    else:
        display.show("N")
        set_speed(14,14)
        
    np.show()