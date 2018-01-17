#
#   Receive and display the temperature
#   and update the NeoPixel panel with 
#   a colour between Blue and Red
#
#   for WWW.PROTO-PIC.CO.UK by Drew Anderson
#

#   import the libraries required by the microbit
from microbit import *
#   import the libraries required by the micro:pixel board & Radio
import neopixel
import radio
#   We have 8x4 pixels - 32 in total on pin 0
np = neopixel.NeoPixel(pin0, 32)
#   Turn the radio transmitter on (Required)
radio.on()

while True:
    # Read any incoming Data
    inData = radio.receive()
    if inData is not None:
        # inData is a string - We want a float
        temp = float(inData)
        # A little bit of maths to extend the scale a bit
        tempcolour = int((temp * 3.6))
        # The next 4 lines constrain the value to between 0 and 127
        if (tempcolour < 0):
            tempcolour = 0
        if (tempcolour > 127):
            tempcolour = 127
        # Update the micro:pixel 
        for pix in range (0 , 32):
            np[pix] = (tempcolour,0,(255-(tempcolour*2)))
        np.show()
        # Show the temperature to 1 decimal place
        tempToShow = "{0:0.1f}".format(temp)
        display.scroll(tempToShow)