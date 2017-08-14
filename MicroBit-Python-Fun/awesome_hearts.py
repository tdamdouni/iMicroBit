from microbit import *

def show_image(image):
    display.show(image)
    sleep(50)
    
def show_centre_pixel():
    display.set_pixel(2, 2, 9)
    sleep(50)
    
def animate_heart():
    show_image(Image.HEART)
    show_image(Image.HEART_SMALL)
    show_centre_pixel()
    display.clear()
    sleep(50)
    show_centre_pixel()
    show_image(Image.HEART_SMALL)
    show_image(Image.HEART)
    sleep(50)

while True:
    animate_heart()
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("BYE!")
        sleep(1000)
        display.clear()
        break
    elif button_a.is_pressed():
        display.scroll("U ROCK!")
    elif button_b.is_pressed():
        display.scroll("U R AWESOME!")
