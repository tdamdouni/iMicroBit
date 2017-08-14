from microbit import *
import radio
radio.on()

while True:
    
    if button_a.was_pressed():
        radio.send('hi')

    if button_b.was_pressed():
        display.clear()

    Happy = radio.receive()
    
    if Happy == 'bye':
        display.show(Image.SAD)
