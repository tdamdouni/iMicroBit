#! /usr/bin/env python

# Sound controlled McRoboFace by Robin Newman June 4th 2016
# requires picon zero hardware plus software library
# see circuitry in article at rbnrpi.wordpress.com
#version 1.2
import piconzero as pz, time

#setup piconzero card
pz.init()
pz.setInputConfig(1,0,True) # used for push button digital input (normally high using internal resistor)
pz.setOutputConfig(5, 3)    # set output 5 to WS2812
pz.setInputConfig(0,1)      # set to Analogue used to sample audio

#initialise variables used by the program
v=0 #adc value
offset=0 #rest adc value read when button pushed
opencount=0 #count cycles between shutting and next opening of mouth
shutcount=0 #count cycles between opening and next shutting of mouth
openFlag=0 #0 closed, 1 open
b=0 #current brightness
threshold=65 #trigger brightness level to open mouth
blast=0 #last brightness
openslot=8 #number of cycles for which mouth remains open (initial value)
shutslot=2 #number of cycles for which mouth remains closed (I have had this higher at 4: experiment with it!)

#define function to open or close mouth
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
    pz.setAllPixels(128,0,128) #set an initial pixel state
    pz.setPixel(15,0,255,0,False) #eye
    pz.setPixel(16,0,255,0) #other eye
    pz.setPixel(14,0,0,255) #nose
    while True:
        #adjust counters depending upon whether mouth open or closed
        if openFlag==1:
            opencount +=1 #increase count of number of cycles mouth is open
        else:
            shutcount+=1 #increase count of number of cycles mouth is closed

        if (b>threshold) and (shutcount>shutslot) and (openFlag==0): #open mouth triggered by audio
            opencount=0 #reset count to 0 
            openslot=int(b/10) #set openslot cycles according to brightness
            openFlag=1 #opening so set flag
            change(1) #open mouth

        else:
            if (opencount >openslot) and (openFlag==1 and b<threshold-20): #ensures stays open for at least openslot cycles
                 openFlag=0 #closing so reset flag
                 #shutslot=2 #doesn't change. set in intialisation
                 shutcount=0 #reset shutcount
                 change(-1) #close mouth

        #now process brigthness level
        v=pz.readInput(0)# read adc value from audio input
        b=min(100,5*(abs(v-offset))+5) #calcuate next brigthness
        print(b) #print to terminal

        #check for offset calibration button
        trigger=pz.readInput(1) #check for button pressed
        if trigger==0: #normally high: 0 if pushed
           offset=v #update offset value from current adc value

        #now adjust brightness if changed sufficiently
        if abs(blast-b)>10: #check if brightness has changed by at least 10 to reduce noise
            pz.setBrightness(b) #update brightness
            pz.updatePixels() #update all pixels
            blast=b #save brightness value

        time.sleep(0.01) #short sleep to keep response time good, just enough to allow ctrl-C to get a look in

except KeyboardInterrupt:
    print
finally:
    pz.cleanup() #reset picon zero board

