from microbit import *
import neopixel
from random import randint

numpixels = 32
np = neopixel.NeoPixel(pin2, numpixels)
bright = 40
numscan = 8

def setPixel(id, val):
    if (id>=0 and id<numscan):
        np[id] = (val, 0, val)
        np[id+8] = (0, val, val)
        np[id+16] = (0, val, val)
        np[id+24] = (val, 0, val)
        #np[id+int(numpixels/2)] = (val, 0, val)

while True:
    for i in range (0, numscan):
        setPixel(i-3, 0)
        setPixel(i-2, 2)
        setPixel(i-1, 10)
        setPixel(i, 40)
        setPixel(i+1, 10)
        setPixel(i+2, 2)
        setPixel(i+3, 0)
        np.show()
        sleep(100)
    for i in range (numscan, 0, -1):
        setPixel(i-3, 0)
        setPixel(i-2, 2)
        setPixel(i-1, 10)
        setPixel(i, 40)
        setPixel(i+1, 10)
        setPixel(i+2, 2)
        setPixel(i+3, 0)
        np.show()
        sleep(100)
