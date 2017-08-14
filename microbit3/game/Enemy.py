from microbit import*
import radio
radio.on()
shot = 0

while True:

    if button_a.was_pressed():
        display.clear()
        radio.send('shot')
        shot = shot + 1

    display.set_pixel(0,shot,9)
    display.set_pixel(1,shot,9)
    display.set_pixel(2,shot,9)
    display.set_pixel(3,shot,9)
    display.set_pixel(4,shot,9)
    
    if button_b.is_pressed():
        display.clear()
        shot = 0   
