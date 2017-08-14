from microbit import *
import random

while True:
    pin0.write_digital(1)
    sleep(random.randint(100, 1000))
    pin0.write_digital(0)
    sleep(random.randint(100, 1000))
