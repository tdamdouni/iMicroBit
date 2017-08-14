from microbit import *


display.clear()

while True:

    if button_a.is_pressed():
        display.clear()
        display.scroll("PIXEL A")
    
    if button_b.is_pressed():
        display.clear()
        display.scroll("MARIO")
        display.set_pixel(0,0,0)
        display.set_pixel(1,0,9)
        display.set_pixel(2,0,9)
        display.set_pixel(3,0,9)
        display.set_pixel(4,0,9)
        display.set_pixel(0,1,0)
        display.set_pixel(1,1,6)
        display.set_pixel(2,1,3)
        display.set_pixel(3,1,3)
        display.set_pixel(4,1,0)
        display.set_pixel(0,2,6)
        display.set_pixel(1,2,9)
        display.set_pixel(2,2,6)
        display.set_pixel(3,2,9)
        display.set_pixel(4,2,6)
        display.set_pixel(0,3,3)
        display.set_pixel(1,3,9)
        display.set_pixel(2,3,9)
        display.set_pixel(3,3,9)
        display.set_pixel(4,3,3)
        display.set_pixel(0,4,6)
        display.set_pixel(1,4,6)
        display.set_pixel(2,4,0)
        display.set_pixel(3,4,6)
        display.set_pixel(4,4,6)
