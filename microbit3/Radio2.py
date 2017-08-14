from microbit import *
import radio
radio.on()

while True:
    
    if button_a.was_pressed():
        radio.send('bye')

    if button_b.was_pressed():
        display.clear()

    Happy = radio.receive()
    
    if Happy == 'hi':
        display.show(Image.HAPPY)
