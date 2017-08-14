"""Accel: shake it!

Shake the micro:bit and see how high you can reach! Press the A button to start
a countdown, when the screen lights up, you have 2 seconds to shake the
micro:bit. It'll then tell you how hard it was shaken.
"""
from microbit import *


display.show(Image.ARROW_W)
while True:
    while not button_a.was_pressed():
        sleep(100)
    for i in range(3, 0, -1):  # The final countdown!
        display.show(str(i))
        sleep(1000)
    display.show(Image().invert())
    shake = 0
    start = running_time()
    while running_time() - start < 2000:  # Shake for 2 seconds.
        values = accelerometer.get_values()
        shake += abs(sum(values) - sum(accelerometer.get_values()))
    display.scroll(str(shake // 1000), loop=True, wait=False)
