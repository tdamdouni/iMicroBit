from microbit import *
import random

# See https://microbit-micropython.readthedocs.io/en/latest/

## Micro event system
## Second evolution

Queue=[]
class ContextClass:
    def __init__(self):
        self.a=False
        self.b=False
        self.fadeParam=-1

def EventLoop(extraSleepTime=0):
    Context=ContextClass()
    while True:
        if(extraSleepTime >0):
            sleep(extraSleepTime)
        for f,t in Queue:
            f(Context)
            if t>0:
                sleep(t)
                
### Functions the event system will call
dots = [ [0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]

def led_dance(c):        
    # A/B pressed?
    ba=c.a
    bb=c.b
    # Turn on a off one if possible
    a=random.randrange(5)
    b=random.randrange(5)
    if( dots[a][b] != 0):
        # II chance choser 
        b=random.randrange(5)
    dots[a][b] = 8
    display.set_pixel(a, b, dots[a][b])
    if ba:
        c.fadeParam=-1
    if bb:
        c.fadeParam=1
    if ba or bb:
        for i in range(5):
            for j in range(5):
                newVal=dots[i][j] + c.fadeParam
                if newVal >8:
                    newVal=8
                elif newVal <0:
                    newVal=0
                dots[i][j] = newVal
                display.set_pixel(i, j, dots[i][j])

    
def buttons_test(c):
    c.a=False
    c.b=False
    if button_a.is_pressed():
        c.a=True
    if button_b.is_pressed():
        c.b=True

# Queue is a tuple with: funtion + sleepTime
# You must sum all the time to get a valid idea on how it works
# 0 means: no sleep at all, execute function and go.
# For instance fot checking every 200ms buttons and updating led dance,
# you should only set the led_dance:
Queue=[ (buttons_test,0), (led_dance,280)]
EventLoop()
