# Light LEDs at random and make them fade over time
#
# Usage:
#
#    led_dance(delay)
#
# 'delay' is the time between each new LED being turned on.
#
# TODO The random number generator is not great. Perhaps the accelerometer
# or compass could be used to add entropy.

import microbit
import random



def led_dance(delay):
    dots = [ [0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]
    while True:
        # Turn on a off one if possible
        a=random.randrange(5)
        b=random.randrange(5)
        if( dots[a][b] != 0):
            # II chance choser 
            b=random.randrange(5)
        dots[a][b] = 8
        microbit.display.set_pixel(a, b, dots[a][b])
        # run turn off cycle sometimes:
        # if I want a lot of thme active
        if random.randrange(8) <=0:
            for i in range(5):
                for j in range(5):
                    microbit.display.set_pixel(i, j, dots[i][j])
                    dots[i][j] = max(dots[i][j] - 1, 0)
        else:
            microbit.sleep(delay)

random.seed(1337)

led_dance(45)
