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

# GG see https://microbit-micropython.readthedocs.io/en/latest/

import microbit
import random



def led_dance(delay):
    dots = [ [0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]
    prob=4
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
        if  microbit.button_a.is_pressed():
            prob=min(prob+1,8)
        if  microbit.button_b.is_pressed():
            prob=max(0, prob-1)
        if random.randrange(8) <= prob :
            for i in range(5):
                for j in range(5):
                    microbit.display.set_pixel(i, j, dots[i][j])
                    dots[i][j] = max(dots[i][j] - 1, 0)    
        microbit.sleep(delay)

random.seed(1337)

led_dance(100)
