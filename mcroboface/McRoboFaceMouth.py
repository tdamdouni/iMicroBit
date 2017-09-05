#! /usr/bin/env python

# McRoboFaceMouth.py
# Test code for 4tronix Picon Zero

import piconzero as pz, time

pz.init()
pz.setOutputConfig(5, 3)    # set output 5 to WS2812

def change(t): #parameter = 1 to open mouth anything else to close it
    #False parameter so all updates done together once set up, when brightness changes
    pz.setPixel(0,128,0,128,False) #end of mouth always this colour
    pz.setPixel(5,128,0,128,False) #other end of mouth

    if t==1: #going for open mouth
        for i in xrange(1,5):#mouth set pixels for open state
            pz.setPixel(i,128,0,128,False)
            pz.setPixel(i+5,128,0,128,False)
        for i in xrange(10,14): #pixels for closed mouth turned off
            pz.setPixel(i,0,0,0,False)
    else: #going for closed mouth
        for i in xrange(1,5): #mouth
            pz.setPixel(i,0,0,0,False)
            pz.setPixel(i+5,0,0,0,False)
        for i in xrange(10,14): #pixels for closed mouth turned on
            pz.setPixel(i,128,0,128,False)
    return

try:
    pz.setAllPixels(128,0,128)
    while True:
        change(1)
        pz.updatePixels()
        time.sleep(0.5)
        change(0)
        pz.updatePixels()
        time.sleep(0.5)
except KeyboardInterrupt:
    print
finally:
    pz.cleanup()

