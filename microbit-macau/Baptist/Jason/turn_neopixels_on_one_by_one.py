# Add your Python code here. E.g.
from microbit import *
from bitbot import *
from neopixel import *


np = NeoPixel(pin13,12)

while True:
    sleep(1000)

    np.clear()
    
    for i in range(0,12):
        np[i] = (0,30,30)
        sleep(1000)
        np.show()