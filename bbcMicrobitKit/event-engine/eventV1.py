from microbit import *
import random

## Micro event system
## First example
## FIXME:
##  Same time for every function
##  Context is boring to setup 
Queue=[]
Context= { "be_happy": True, "a": False, "b": False, "prob": -1 }


def EventLoop(sleepTime):
    while True:
        for f in Queue:
            f(Context)
            sleep(sleepTime)

### Functions the event system will call

dots = [ [0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]

def led_dance(c):    
    prob=c["prob"]
    # A/B pressed?
    ba=c["a"]
    bb=c["b"]
    # Turn on a off one if possible
    a=random.randrange(5)
    b=random.randrange(5)
    if( dots[a][b] != 0):
        # II chance choser 
        b=random.randrange(5)
    dots[a][b] = 8
    display.set_pixel(a, b, dots[a][b])
    # run turn off cycle sometimes:
    # if I want a lot of thme active
    # if  ba:
    #     prob=min(prob+1,8)
    # if  bb:
    #     prob=max(0, prob-1)
    if ba:
        #if random.randrange(8) <= prob :
        for i in range(5):
            for j in range(5):                
                dots[i][j] = max(dots[i][j] - 1, 0)
                display.set_pixel(i, j, dots[i][j])
    # Record the prob
    c["prob"]=prob
    
def buttons_test(c):
    c["a"]=False
    c["b"]=False
    if button_a.is_pressed():
        c["a"]=True
    if button_b.is_pressed():
        c["b"]=True

# def happy(c):
#     if c["be_happy"]:
#         display.show(Image.HAPPY)

# def sad(c):
#     if c["be_happy"] == False:
#         display.show(Image.SAD)

Queue=[ buttons_test, led_dance]
EventLoop(20)
