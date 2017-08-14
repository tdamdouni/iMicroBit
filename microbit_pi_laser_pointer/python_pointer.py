# Script to receive data from the microbit and use that data to move our laser pointer
# THIS SCRIPT BELONGS ON THE RASPBERRY PI

import RPi.GPIO as GPIO
import serial
import time

# Set the variables that concern our serial communication 
PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

### Set the variables that control our servos
servo1 = 23
servo2 = 32
pointer_startx = 6
pointer_starty = 6


# This loop will take incoming tilt data and convert it to numbers our servo can use
# Through testing, the servos have a pwm range between 3 and 9.  Your servos may be different
# Through testing, fulltilt appears to be 1000, reduced max val for ease of use
def get_servo_value(myval):
  # Set variables we will use to convert data to servo movement, create coefficient
  # Put point 0 on everything to insure float calculation
  servo_min = 3.0
  servo_max = 9.0
  tilt_max = 976.0
  full_tilt = tilt_max * 2.0
  new_val = tilt_max + myval        # This compensates for negative values
  move_val = abs(new_val)/full_tilt * (servo_max - servo_min) + servo_min
  return move_val

# Turns on gpio, moves serve, and then turns off the gpio
# Note: from other experiments, it is best to turn off each GPIO after use
# Irregularities in the Pi's signal output cause servos to twitch if not turned off
def move_servo(myservo, mymove):
  # Set top servo position
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(myservo,GPIO.OUT)
  pwm=GPIO.PWM(myservo,50)
  pwm.start(5)
  pwm.ChangeDutyCycle(mymove)
  time.sleep(1)
  GPIO.cleanup()

# Loop forever gathering data from hub microbit, converting the data for servo use,
# printing servo value, and activating servos
while True:
  # Get The Data
  data = s.readline().decode('UTF-8')   #check for data.  this code blocks script from moving forward until data is received.
  datalist = data.rstrip().split(',')

  # Convert the data to movement. 
  current_x = get_servo_value(int(datalist[0]) * -1)
  current_y = get_servo_value(int(datalist[1]))
  
  # Print current vals to console
  print("x is %d" % int(datalist[0]))
  print("y is %d" % int(datalist[1]))

  # UNCOMMENT TO USE SERVOS
  # Set current servo positions
  move_servo(servo1, current_y)
  time.sleep(1)
  move_servo(servo2, current_x)


