#
# Traffic Light with Pedestrian Crossing
#

from microbit import *

# We are just using a buzzer for one tone,
# but this include is the easiest way to do this
import music

# Run this over and over forever
while True:
    # Set the traffic light to GO
    pin13.write_digital(0)
    pin2.write_digital(1)
    pin12.write_digital(1)
    # Read the button, if it is pressed then
    # do the crossing animation
    if button_a.is_pressed():
        # Now do the crossing routine
        pin13.write_digital(1)
        sleep(5000)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(1000)
        pin1.write_digital(0)
        pin16.write_digital(1)
        sleep(2000)
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin13.write_digital(0)
        for counta in range(0,40):
            music.pitch(1600, 100)
            sleep(80)
        for countb in range (0,10):
            pin8.write_digital(0)
            sleep(200)
            pin8.write_digital(1)
            sleep(200)
        pin8.write_digital(0)
        pin12.write_digital(1)
        sleep(2000)
        pin1.write_digital(1)
        sleep(1000)
        pin1.write_digital(0)
        pin2.write_digital(1)
        pin16.write_digital(0)
        # Now we keep traffic moving for at least 30 Seconds
        # stops the crossing from being permanently on
        sleep(30000)
