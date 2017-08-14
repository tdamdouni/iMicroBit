from microbit import *

x=0

while button_a.is_pressed() == False:
    if accelerometer.was_gesture('up'):
        x=x+1
        
if button_a.is_pressed():
    display.scroll(str(x))
