# microbit.py  15/09/2015  D.J.Whale

import time

#----- CONFIGURATION -----------------------------------------------------------

DEBUG                 = False
USE_EMBEDDED_PYSERIAL = True
BAUD                  = 115200

if USE_EMBEDDED_PYSERIAL:
  from os import sys, path
  thisdir = path.dirname(path.abspath(__file__))
  sys.path.append(thisdir)
  
import serial


#----- PORTSCAN ----------------------------------------------------------------

import portscan

name = portscan.getName()
if name != None:
  if DEBUG:
    print("Using port:" + name)
  PORT = name
else:
  name = portscan.find()
  if name == None:
    raise ValueError("No port selected, giving in")
  PORT = name
  print("Your micro:bit has been detected")
  print("Now running your program...")


#----- CONFIGURE SERIAL PORT ---------------------------------------------------

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

s.close()
s.port = PORT
s.open()


#----- SERIAL PORT ACCESSORS --------------------------------------------------

line_buffer = ""
rec_buffer = None


def readWaiting():
  global rec_buffer
  if rec_buffer != None:
    return True

  line = processSerial()
  if line != None:
    rec_buffer = line
    return True

  return False


def read():
  global rec_buffer

  if not readWaiting():
    return None

  rec = rec_buffer
  rec_buffer = None
  #print("read:" + rec)
  return rec


def processSerial():
  global line_buffer

  while True:
    data = s.read(1)
    if len(data) == 0:
      return None # no new data has been received
    data = data[0]

    if data == '\n':
      pass # strip newline

    elif data[0] == '\r':
      line = line_buffer
      line_buffer = ""
      #print(line)
      return line

    else:
      line_buffer += data


#----- TRANSPORT ADAPTOR ------------------------------------------------------

def send(msg):
    msg += '\r\n'
    for tx in msg:
        #print(tx)
        s.write(tx)
        rx = s.read(1) # set timeout of 1 sec, if don't get prompt, error recovery CTRL-C wait prompt with timeout?
        if tx != rx:
          print("diff")
          # error recovery, CTRL-C wait for prompt with timeout?


def get():
  while True:
    line = read()
    if line != None:
      return line
    time.sleep(0.1)


# END
