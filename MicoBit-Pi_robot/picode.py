import serial
from time import sleep
import RPi.GPIO as GPIO # Import the GPIO Library


#MicroBit Stuff------------------------------------------
#Setup Serial Port
PORT = "/dev/ttyACM0"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
#read the first line and flush any bad data
s.readline()

#Function to Get 2 buttons and xyz
def read_microbit_data():
    #read a line from the microbit, 
    data = s.readline()
    #split the microbit data into x, y, z, a, b
    data_s = data.rstrip().split(" ")
    x, y, z = int(data_s[0]), int(data_s[1]), int(data_s[2])
    a = True if data_s[3] == "True" else False
    b = True if data_s[4] == "True" else False
    #debug
    #print(x, y, z)
    #print(a, b)
    return x, y, z, a, b

#Setup Robot
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
 GPIO.output(pinMotorAForwards, 0)
 GPIO.output(pinMotorABackwards, 0)
 GPIO.output(pinMotorBForwards, 0)
 GPIO.output(pinMotorBBackwards, 0)

 # Turn both motors forwards
def Forwards():
 GPIO.output(pinMotorAForwards, 1)
 GPIO.output(pinMotorABackwards, 0)
 GPIO.output(pinMotorBForwards, 1)
 GPIO.output(pinMotorBBackwards, 0)

 # Turn both motors backwards
def Backwards():
 GPIO.output(pinMotorAForwards, 0)
 GPIO.output(pinMotorABackwards, 1)
 GPIO.output(pinMotorBForwards, 0)
 GPIO.output(pinMotorBBackwards, 1)
 
 
 # Turn left
def Right():
 GPIO.output(pinMotorAForwards, 0)
 GPIO.output(pinMotorABackwards, 1)
 GPIO.output(pinMotorBForwards, 1)
 GPIO.output(pinMotorBBackwards, 0)

 
 # Turn Right
def Left():
 GPIO.output(pinMotorAForwards, 1)
 GPIO.output(pinMotorABackwards, 0)
 GPIO.output(pinMotorBForwards, 0)
 GPIO.output(pinMotorBBackwards, 1)
	
	
	
	
	
#Main loop
try:

    
    while True:
        x, y, z, a, b = read_microbit_data()
        if a:
            print ("forward")
            Forwards()
        if b:
            print ("stop")
            StopMotors()
        if x > 750:
            print ("right")
            Right()
        if x < -750:
            print ("left")
            Left()
        if y > 750:
            print ("backwards")
            Backwards()
        if y < -750:
            print ("forward")
            Forwards()
finally:
    sleep(1)
    s.close()
