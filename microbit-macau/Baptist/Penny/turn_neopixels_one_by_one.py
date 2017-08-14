from microbit import*
from bitbot import*
from neopixel import*

while True:
    np=NeoPixel(pin13,12)
    for abc in range(0,12):
        np[abc]=(2,2,0)
        np.show()
        sleep(1000)
        
    np.clear()

