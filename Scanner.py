from microbit import *
import neopixel
from random import randint

numpixels = 12
np = neopixel.NeoPixel(pin13, numpixels)
bright = 40

def setPixel(id, val):
    if (id>=0 and id<=5):
        np[id] = (val, 0, val)
        np[id+6] = (val, 0, val)

while True:
    for i in range (0, 6):
        setPixel(i-3, 0)
        setPixel(i-2, 2)
        setPixel(i-1, 10)
        setPixel(i, 40)
        setPixel(i+1, 10)
        setPixel(i+2, 2)
        setPixel(i+3, 0)
        np.show()
        sleep(100)
    for i in range (6, 0, -1):
        setPixel(i-3, 0)
        setPixel(i-2, 2)
        setPixel(i-1, 10)
        setPixel(i, 40)
        setPixel(i+1, 10)
        setPixel(i+2, 2)
        setPixel(i+3, 0)
        np.show()
        sleep(100)
