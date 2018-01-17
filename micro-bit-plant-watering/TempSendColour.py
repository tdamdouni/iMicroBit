#
#   Read and display the temperature
#   and update the NeoPixel panel with 
#   a colour between Blue and Red, and
#   send the data to any listening node 
#
#   (The micro:pixel panel is not needed)
#
#   for WWW.PROTO-PIC.CO.UK by Drew Anderson
#

#   import the libraries required by the microbit
from microbit import *
#   import the libraries required by the micro:pixel and Radio
import neopixel
import radio

#   We have 8x4 pixels, 32 in total on pin 0
np = neopixel.NeoPixel(pin0, 32)

while True:
    # Read the RAW temperature
    tmp = pin1.read_analog()
    # Convert the RAW to a real Temperature
    temp = ((tmp * (3300.0/1024.0))-500.0)/10.0
    # Expand the scale for better display in micro:pixel
    tempcolour = int((temp * 3.6))
    # The next 4 lines constrain the colour value to 0 <> 127
    if (tempcolour < 0):
        tempcolour = 0
    if (tempcolour > 127):
        tempcolour = 127
    # Show the colour on the micro:pixel
    for pix in range (0 , 32):
        np[pix] = (tempcolour,0,(255-(tempcolour*2)))
    np.show()
    # Show the Temperature to one decimal place
    tempToShow = "{0:0.1f}".format(temp)
    display.scroll(tempToShow)
    # Turn on the radio
    radio.on()
    # Send the temp as a string
    radio.send(str(temp))
    # Let the data finish
    sleep(50)
    # Turn off the radio to save battery
    radio.off()
    sleep(50)

    