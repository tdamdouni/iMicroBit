from microbit import *

while True:
    if pin0.is_touched():
        display.scroll("say cheese!")
        sleep(500)
        pin1.write_digital(1)
        sleep(5000)
