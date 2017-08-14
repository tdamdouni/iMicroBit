# neopixel_controller
# by Michael Saunby   http://mike.saunby.net
# Copy, adapt, etc. as you wish.
#
from microbit import *
import neopixel

# Using the default setting retains compatibility with the console, and 
# serves to remind me of the baud rate required.
uart.init(115200)

# Setup the Neopixel strip on pin0 with a length of 150 pixels
npA = neopixel.NeoPixel(pin0, 150)
#npB = neopixel.NeoPixel(pin1, 150)
#npC = neopixel.NeoPixel(pin2, 150)

npA[0] = (255,0,0)
npA[1] = (0,255,0)
npA[2] = (0,0,255)
npA.show()

uart.write("?")
inbytes = bytearray()
while True:
    c = uart.read(1)
    if c != None:
        if c == b'\r':
            # received return char so now process line
            uart.write(" return!!\n\r")
            ar = str(bytes(inbytes).format()).split(",")
            if len(ar) == 4:
                nums = []
                for n in ar:
                    nums.append(int(n))
                uart.write( str(nums) )
                npA[nums[0]] = (nums[1],nums[2],nums[3])
                npA.show()
            else:
                pass
            inbytes = bytearray()
        else:
            inbytes.extend(c)
            #text = bytes(inbytes).strip().format()
            #uart.write("Your text :" + text + "\n\r")

        uart.write("?")
        #display.scroll("hello")
    sleep(2)
