from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 32)

while True:
    tmp = pin1.read_analog()
    temp = ((tmp * (3300.0/1024.0))-500.0)/10.0
    display.scroll(str(temp))
    tempcolour = int((temp * 3.6))
    for pix in range (0,32):
        np[pix] = (tempcolour,0,(255-(tempcolour*2)))
    np.show()
    
