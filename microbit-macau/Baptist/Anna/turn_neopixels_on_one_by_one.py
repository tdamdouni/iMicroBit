# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *


while True:
    np = NeoPixel(pin13,12)
    for a in range(0,11):
        np[a]=(25,10,0)
    np.show()
    sleep(1000)
    np.clear()
    sleep(1000)
    
    
    
    
    