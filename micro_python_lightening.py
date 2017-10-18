from microbit import *
import neopixel
from random import randint

#set up the 4 neopixels on pin 0
np = neopixel.NeoPixel(pin0,4)


while True:
    if button_a.is_pressed():
        while True:
            #get a random light number
            randButton = randint(0,3)
            
            #TEST display the light that's flashing
            #display.show(str(randButton))
            
            #set the random light to white, show, flash twice
            np[randButton] = (255, 255, 255)
            np.show()
            sleep(100)
            np.clear()
            
            sleep(150)
            
            np[randButton] = (255, 255, 255)
            np.show()
            sleep(400)
            np.clear()

            #randomly sleep between flashing lights
            randSleep = randint(500, 1500)
            sleep(randSleep)



        
    if button_b.is_pressed():
        #rainbow time! cycle through the rainbow colours 3 times
        for x in range (0,3):
            np[0] = (255, 0, 0)
            np.show()
            sleep(300)
            np.clear()
            
            np[1] = (255, 127, 0)
            np.show()
            sleep(300)
            np.clear()
            
            np[2] = (255, 255, 0)
            np.show()
            sleep(300)
            np.clear()
            
            np[3] = (0, 255, 0)
            np.show()
            sleep(300)
            np.clear()
            
            np[0] = (0, 0, 255)
            np.show()
            sleep(300)
            np.clear()
            
            np[1] = (75, 0, 130)
            np.show()
            sleep(300)
            np.clear()
            
            np[2] = (139, 0, 255)
            np.show()
            sleep(300)
            np.clear()        
        
            sleep(1000)

        #scare them with some more lightening at the end
        for x in range (0,4):
            np[0]=(255,255,255)
            np[1]=(255,255,255)
            np[2]=(255,255,255)
            np[3]=(255,255,255)
            np.show()
            sleep(100)
            np.clear()
            sleep(200)