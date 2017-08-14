from microbit import *
import radio
radio.on()
radio.config(channel=86)
def output(data):
    radio.send(str(data))
    data = str(data)
    if len(data) == 1:
        display.show(data)
    else:
        display.scroll(data)

def is_up():
    y1 = accelerometer.get_y()
    sleep(250)
    y2 = accelerometer.get_y()
    if y2 - y1 >= 180:
        return True
    else:
        return False
def is_step():
    if is_up:
        output("1")
    else:
        output("0")
        
    
while True:
    is_step()
    sleep(125)
    