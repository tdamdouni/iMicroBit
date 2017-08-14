# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *


np = NeoPixel(pin13,12)

for i in range(0,12):
    np[i] = (40,0,40)
np.show()

def dark_left():
    return not button_b.is_pressed()

def dark_right():
    return not button_a.is_pressed()

while True:


    
    if dark_left() and dark_right() :
        for i in range(0,12):
            np[i] = (40,0,40)
        np.show()
        display.show("B")
        set_speed(20,20)
        sleep(10)
        
        
    elif dark_right():
        for i in range(0,12):
            np[i] = (30,30,0)
        np.show()
        display.show("R")
        set_speed(60,10)
        sleep(10)
        
    elif dark_left():
        for i in range(0,12):
            np[i] = (0,0,40)
        np.show()
        display.show("L")
        set_speed(15,75)
        sleep(10)
        
    else:
        for i in range(0,12):
            np[i] = (20,30,0)
        np.show()
        display.show("N")
        set_speed(0,0)
        sleep(10)


