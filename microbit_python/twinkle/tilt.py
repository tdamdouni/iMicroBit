from microbit import *
from neopixel import *

n = NeoPixel(pin0, 8)
RED = (255, 0, 0)
OFF = (0, 0, 0)
while True:
    a = abs(accelerometer.get_y() / 128)-1
    for i in range(7,a,-1):
        n[i] = OFF
    for i in range(a):
        n[i] = RED
    n.show()
    sleep(100)