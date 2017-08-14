# Add your Python code here. E.g.
from microbit import *


while True:
    pin0.write_digital(0)
    pin1.write_digital(1)
    sleep(2000)
    pin0.write_digital(1)
    pin1.write_digital(0)
    sleep(2000)


