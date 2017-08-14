# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *

def dark_left():
    return not button_b.is_pressed()
    
def dark_right():
    return not button_a.is_pressed()
    
np = NeoPixel(pin13,12)
for i in range(0,12):
    np[i] = (30,10,0)
np.show()


while True:
    

        
    if dark_left() and dark_right():
        for i in range(0,12):
            np[i] = (100,100,100)
        np.show()
        display.show("B")
        set_speed(40,40)
        sleep(10)
    elif dark_right():
        for i in range(0,12):
            np[i] = (0,0,100)
        np.show()
        display.show("R")
        set_speed(40,0)
        sleep(10)
    elif dark_left():
        for i in range(0,12):
            np[i] = (30,0,0)
        np.show()
        set_speed(0,40)
        sleep(10)
        display.show("L")
    else:
        display.show("N")
        for i in range(0,12):
            np[i] = (30,30,0)
        np.show()
        set_speed(0,0)
        sleep(10)
            
    
    