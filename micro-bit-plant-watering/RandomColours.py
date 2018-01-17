from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 4 pixels
np = neopixel.NeoPixel(pin0, 32)

while True:
    for thisloop in range(0,100):
        for pixel_id in range(0, 32):
            red = randint(0, 50)
            green = randint(0, 50)
            blue = randint(0, 50)
            np[pixel_id] = (red, green, blue)
        np.show()
        sleep(randint(10,100))
    for colour in range (0,128):
        for pixel_id in range(0, 32):
            np[pixel_id] = (colour, 0, 0)
        np.show()
        sleep(10)
    for colour in range (0,128):
        for pixel_id in range(0, 32):
            np[pixel_id] = (128 - colour, colour, 0)
        np.show()
        sleep(10)    
    for colour in range (0,128):
        for pixel_id in range(0, 32):
            np[pixel_id] = (0, 128-colour, colour)
        np.show()
        sleep(10)
