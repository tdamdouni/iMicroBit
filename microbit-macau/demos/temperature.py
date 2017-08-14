from microbit import *

display.show(Image.ARROW_W)
while True:
    if button_a.get_presses() > 0:
        temp = temperature()
        display.scroll(str(temp) + " C")
        display.show(Image.ARROW_W)

    sleep(300)
