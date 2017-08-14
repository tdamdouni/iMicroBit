from microbit import *
import music

A = False
B = False
PITCH = 440

# PIN2 read_analog()
ACTION_VALUE = 50
VOLUMEUP_VALUE = 150
VOLUMEDOWN_VALUE = 350
#nothing: 944

prev_l = False
prev_r = False
l = False
r = False

while True:
    v = pin2.read_analog()
    if v < ACTION_VALUE:
        l,r = True, True
    elif v < VOLUMEUP_VALUE:
        l,r = False, True 
    elif v < VOLUMEDOWN_VALUE:
        l,r = True, False
    else:
        l,r = False, False
       
    if l != prev_l: 
        prev_l = l
        if l:
            music.pitch(PITCH, pin=pin0)
            display.set_pixel(0,2,9)
        else:
            display.set_pixel(0,2,0)
            music.stop(pin0)
        
    if r != prev_r:
        prev_r = r
        if r:
            display.set_pixel(4,2,9)
            music.pitch(PITCH, pin=pin1)
        else:
            display.set_pixel(4,2,0)
            music.stop(pin1)
            
        
