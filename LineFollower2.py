# Add your Python code here. E.g.
from microbit import *

leftA = pin0
leftB = pin8
rightA = pin1
rightB = pin12
leftLine = pin11
rightLine = pin5
speedFwd = 100
speedTurn = 40

def reverse (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(1023-spd)
    leftB.write_digital(1)
    rightA.write_analog(1023-spd)
    rightB.write_digital(1)

def forward (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(spd)
    leftB.write_digital(0)
    rightA.write_analog(spd)
    rightB.write_digital(0)

def spinLeft (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(1023-spd)
    leftB.write_digital(1)
    rightA.write_analog(spd)
    rightB.write_digital(0)

def softLeft (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(350)
    leftB.write_digital(1)
    rightA.write_analog(spd)
    rightB.write_digital(0)

def spinRight (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(spd)
    leftB.write_digital(0)
    rightA.write_analog(1023-spd)
    rightB.write_digital(1)

def softRight (spdpct):
    spd = spdpct * 10.23
    leftA.write_analog(spd)
    leftB.write_digital(0)
    rightA.write_analog(350)
    rightB.write_digital(1)

def stop():
    leftA.write_analog(0)
    leftB.write_digital(0)
    rightA.write_analog(0)
    rightB.write_digital(0)

lastfwd = 0
while True:
    lline = leftLine.read_digital()
    rline = rightLine.read_digital()
    if((lline == 1) and (rline == 0)):
        softLeft(speedTurn)
        #sleep(1)
        lastfwd = 0
        while ((leftLine.read_digital() == 1) and (rightLine.read_digital() == 0)):
            pass
            #sleep(1)
    elif((rline == 1) and (lline == 0)):
        softRight(speedTurn)
        #sleep(1)
        lastfwd = 0
        while ((rightLine.read_digital() == 1) and (leftLine.read_digital() == 0)):
            pass
            #sleep(1)
    else:
        if (lastfwd == 0):
            forward(speedFwd)
        lastfwd = 1
    
    
