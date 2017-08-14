from microbit import *
import radio


BEACON_NAME = 'lift'
RATE_MS = 1000
START_POWER = 0 # lowest 0=-30dBm


radio.config(power=START_POWER) # lowest power 0=-30dBm
radio.on()

while True:
    display.show(Image.DIAMOND_SMALL)
    sleep(RATE_MS)
    display.show(Image.DIAMOND)
    
    radio.send(BEACON_NAME)
    sleep(250) # leave image on display a bit longer
    
 
    