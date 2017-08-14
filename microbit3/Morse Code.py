from microbit import *
import radio
radio.on()

while True:
    
    if button_a.was_pressed():
        radio.send('.')

    if button_b.was_pressed():
        radio.send('-')
        message  = radio.receive()

    if message == '.':
        display.clear()
        sleep (100)
        display.set_pixel(2,2,9)

    if message == '-':
        display.clear()
        sleep (100)
        display.show("-")     
