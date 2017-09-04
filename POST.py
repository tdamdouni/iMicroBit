#Power On Self Test: tests all/most functions of Bit:Bot
from microbit import *
import neopixel

leftA = pin0
leftB = pin8
rightA = pin1
rightB = pin12
leftLine = pin11
rightLine = pin5
buzzer = pin14
lightSensor = pin2
lightSelect = pin16
np = neopixel.NeoPixel(pin13, 12)

sleepDel = 800

def forward():
    leftA.write_digital(1)
    leftB.write_digital(0)
    rightA.write_digital(1)
    rightB.write_digital(0)

def reverse():
    leftA.write_digital(0)
    leftB.write_digital(1)
    rightA.write_digital(0)
    rightB.write_digital(1)

def stop():
    leftA.write_digital(0)
    leftB.write_digital(0)
    rightA.write_digital(0)
    rightB.write_digital(0)

def showAll(red,green,blue):
    for i in range(12):
        np[i] = (red,green,blue)
    np.show()

def showLeftLine():
    aset = leftLine.read_digital() * 9
    for i in range(4):
        display.set_pixel(0,i,aset)
    display.set_pixel(0,4,9)
    
def showRightLine():
    aset = rightLine.read_digital() * 9
    for i in range(4):
        display.set_pixel(4,i,aset)
    display.set_pixel(4,4,9)

def showLight():
    lightSelect.write_digital(0)
    leftLight = lightSensor.read_analog()
    lightSelect.write_digital(1)
    rightLight = lightSensor.read_analog()
    for i in range(5):
        if leftLight > i*200:
            display.set_pixel(1,4-i,9)
        else:
            display.set_pixel(1,4-i,0)
        if rightLight > i*200:
            display.set_pixel(3,4-i,9)
        else:
            display.set_pixel(3,4-i,0)
    
while True:
    forward()
    showAll(50,0,0)
    showLeftLine()
    showRightLine()
    showLight()
    sleep(sleepDel)
    stop()
    showAll(0,50,0)
    showLeftLine()
    showRightLine()
    showLight()
    sleep(sleepDel)
    stop()
    reverse()
    showAll(0,0,50)
    showLeftLine()
    showRightLine()
    showLight()
    sleep(sleepDel)
    stop()
    showAll(50,50,50)
    buzzer.write_digital(1)
    showLeftLine()
    showRightLine()
    showLight()
    sleep(sleepDel)
    buzzer.write_digital(0)
    stop()