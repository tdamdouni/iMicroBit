from microbit import *

while True:
    reading = pin0.read_analog()
    if (reading < 800):
        # Turn on the pump and let it run for 2 seconds
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
        # Wait for 10 seconds to allow
        # water to soak into the soil
        sleep(10000)
