#! /usr/bin/env python

#McRoboFlicker.py
# Sound controlled McRoboFace by Robin Newman June 4th 2016
# requires picon zero hardware plus software library
# see circuitry in article at rbnrpi.wordpress.com

import piconzero as pz, time

pz.init()
pz.setInputConfig(1,0,True) # used for push button digital input (normally high using internal resistor)
pz.setOutputConfig(5, 3)    # set output 5 to WS2812
pz.setInputConfig(0,1)      # set to Analogue used to sample audio

try:
    pz.setAllPixels(128,0,128) #set an initial pixel state
    pz.setPixel(15,0,255,0,False) #eye
    pz.setPixel(16,0,255,0) #other eye
    pz.setPixel(14,0,0,255) #nose
    while True:
        v=pz.readInput(0)# read adc value from audio input
        print(v) #print to terminal
        pz.setBrightness(v) #update brightness
        pz.updatePixels() #update all pixels
        time.sleep(0.01) #short sleep to keep repsonse time good, just enough to allow ctrl-C to get a look in

except KeyboardInterrupt:
    print
finally:
    pz.cleanup() #reset picon zero board

