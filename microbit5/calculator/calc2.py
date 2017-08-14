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
while True:
    msg = radio.receive()
    if msg:
        output(msg)