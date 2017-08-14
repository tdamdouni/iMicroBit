from microbit import *
import microbit

print('Temperature Readings Once Every 15 Seconds\n')

timeElapsed = 0;

delaySecs = 15;

millisPerSec = 1000;

delayTime = delaySecs * millisPerSec;

while(True):
    temp = microbit.temperature();
    
    display.scroll(str(temp))
    
    print("Temperature after " + str(timeElapsed) + " seconds: " + str(temp))
    
    sleep(delayTime)
    timeElapsed += delaySecs;
    
    if button_a.was_pressed():
        print("STOP")
        display.show("X")
        break;