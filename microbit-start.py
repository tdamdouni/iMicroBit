from microbit import *

startup = 0

while True:
    if startup == 0:
        display.scroll("Started")
        startup = 1
    else:
        display.show(Image.HEART)
        if button_a.is_pressed():
            display.show("Text")
            sleep(500)
            display.clear()
        elif button_b.is_pressed():
            display.show("Text2")
            sleep(500)
            display.clear()
