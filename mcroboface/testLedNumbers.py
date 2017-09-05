#! /usr/bin/env python

#testLedNumbers.py
# Testing McRoboFace led positions.
# requires picon zero hardware plus software library


import piconzero as pz, time


pz.init()
pz.setOutputConfig(5, 3)    # set output 5 to WS2812 (code 3)

try:
    while True:
        for i in xrange(0,17):
            pz.setPixel(i,0,0,255)
            time.sleep(0.5)
        pz.setAllPixels(0,0,0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print
finally:
    pz.cleanup() #reset picon zero board
