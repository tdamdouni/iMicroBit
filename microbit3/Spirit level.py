from microbit import *

while True:
    
    reading = accelerometer.get_x()

    if reading > 20:
        display.show("]")

    elif reading < -20:
        display.show("[")

    else:
        display.show("-")
