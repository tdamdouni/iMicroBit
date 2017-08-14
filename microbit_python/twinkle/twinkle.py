from microbit import *
from neopixel import *
import random

MAX = 60
n = NeoPixel(pin0, 8)

while True:
    i=random.randrange(8)
    r=random.randrange(MAX)
    g=random.randrange(MAX)
    b=random.randrange(MAX)
    n[i]=(r,g,b)
    n.show()
    sleep(10)

