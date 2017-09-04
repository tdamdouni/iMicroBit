from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 12)
bright = 40

leftA = pin0
leftB = pin8
rightA = pin1
rightB = pin12
sonar = pin15

gospeed = 100

def getDistance():
    start = running_time()
    for i in range(100):
        sonar.write_digital(1) # Send 10us pulse to trigger
        sleep(0.01)
        sonar.write_digital(0)
        #while sonar.read_digital()==0: #and running_time()-count<0.1: # wait for echo signal to go high
        #    pass
        while sonar.read_digital()==1: #and running_time()-count<0.1: # wait for echo to go low again
            pass
    stop = running_time()
    elapsed = (stop-start-16)/3.77
    distance = int(elapsed)
    return distance

def forward (speedpct):
    setAll(0,bright,0)
    speed = speedpct * 10.23
    leftA.write_analog(speed)
    leftB.write_digital(0)
    rightA.write_analog(speed)
    rightB.write_digital(0)

def reverse (speedpct):
    setAll(bright,0,0)
    speed = speedpct * 10.23
    leftA.write_analog(1023-speed)
    leftB.write_digital(1)
    rightA.write_analog(1023-speed)
    rightB.write_digital(1)

def spinLeft (speedpct):
    setAll(0,0,bright)
    speed = speedpct * 10.23
    leftA.write_analog(1023-speed)
    leftB.write_digital(1)
    rightA.write_analog(speed)
    rightB.write_digital(0)

def spinRight (speedpct):
    setAll(bright,0,bright)
    speed = speedpct * 10.23
    leftA.write_analog(speed)
    leftB.write_digital(0)
    rightA.write_analog(1023-speed)
    rightB.write_digital(1)

def stop():
    leftA.write_analog(0)
    leftB.write_digital(0)
    rightA.write_analog(0)
    rightB.write_digital(0)

def setAll(red,green,blue):
    for idx in range(12):
        np[idx] = (red,green,blue)
    np.show()
    
while True:
    forward(gospeed)
    dist = getDistance()
    if (dist < 15):
    #if (False):
        stop()
        #display.scroll(str(dist))
        #sleep(3000)
        reverse(gospeed)
        sleep(800)
        spinRight(gospeed)
        sleep(200)
        forward(gospeed)