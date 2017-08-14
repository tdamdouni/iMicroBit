# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *

def dark_left():
    return not button_b.is_pressed()
    
def dark_right():
    return not button_a.is_pressed()
    
np = NeoPixel(pin13,12)


while True:
    
    sleep(10)

    np.clear()
    
    for i in range(0,12):
        np[i] = (30,30,0)
        sleep(10)
        np.show()
        
    if dark_left() and dark_right():
        display.show("B")
    elif dark_right():
        display.show("R")
    elif dark_left():
        display.show("L")
    else:
        display.show("N")
            
    
    