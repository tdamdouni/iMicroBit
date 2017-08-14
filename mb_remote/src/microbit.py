# microbit.py  15/09/2015  D.J.Whale
#
# The master-end of a master/slave setup, where the master is a PC/Mac/Pi
# and the slave is a BBC micro:bit
#
# methods in this file are translated to repl instructions sent to the BBC micro:bit
# where they are interpreted and results sent back to this master.
#
# This allows you to write native python programs on various large platforms,
# where sensing and output occurs remotely on the BBC micro:bit

#def __dir__():
#  return [
#    "random", "sleep", "system_time",
#    "compass", "accelerometer",
#    "button_a", "button_b",
#    "display", "io"
#  ]

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


def flush(waitfor='>>> '):
  # find the prompt on startup
  stuff = ""
  while True:
      rx = s.read(1)
      stuff += rx
      if len(stuff) > 3 and stuff[-4:] == waitfor: break
  #if stuff != "":
  #  print('*' * 80)
  #  print(stuff)
  #  print('*' * 80)


def get():
  while True:
    line = read()
    if line != None:
      return line
    time.sleep(0.1)


def prompt():
  flush('>>> ')


def send_nores(line):
  send(line)
  prompt()


def send_res(line):
  send(line)
  result = get()
  prompt()
  return result


def send_res_bool(line):
  result = send_res(line)
  if result == 'True':
    return True
  return False


def send_res_int(line):
  return int(send_res(line))


#----- FUNCTIONS --------------------------------------------------------------

def random(limit):
  return send_res_int("random(%s)" % limit)

def sleep(ms):
  send_nores("sleep(%d)" % ms)


def system_time():
  return send_res("system_time()")

# Note, we don't define print, there is no point, all it does is echo data
# back via the serial port. Handling multiple lines could be tricky, so don't bother.


# ----- COMPASS ---------------------------------------------------------------

class Compass():
  def heading(self):
    return send_res_int("compass.heading()")

  def is_calibrated(self):
    return send_res_bool("compass.is_calibrated()")

  def calibrate(self):
    send_nores("compass.calibrate()")

  def is_calibrating(self):
    return send_res_bool("compass.is_calibrating()")

  def clear_calibration(self):
    send_nores("compass.clear_calibration()")

  def get_x(self):
    return send_res_int("compass.get_x()")

  def get_y(self):
    return send_res_int("compass.get_y()")

  def get_z(self):
    return send_res_int("compass.get_z()")

compass = Compass()


# ----- BUTTON ----------------------------------------------------------------

class Button():
  def __init__(self, index):
    self.index = index

  def is_pressed(self):
    return send_res_bool("button_%s.is_pressed()" % self.index)

button_a = Button('a')
button_b = Button('b')


# ----- ACCELEROMETER ---------------------------------------------------------

class Accelerometer():
  def get_x(self):
    return send_res_int("accelerometer.get_x()")

  def get_y(self):
    return send_res_int("accelerometer.get_y()")

  def get_z(self):
    return send_res_int("accelerometer.get_z()")

accelerometer = Accelerometer()


# ----- DISPLAY ---------------------------------------------------------------

class Image():
  def set_pixel_value(self, x, y, i=255):
    send_nores("display.set_pixel_value(%d,%d,%d)" % (x, y, i))

class Display():
  image = Image()

  #def print(s, i=100):
  # pass

  def scroll(self, m, i=100):
    send_nores("display.scroll(\"%s\", %d)" % (m, i))

  def clear(self):
    send_nores("display.clear()")

display = Display()


# ----- IO ---------------------------------------------------------------

class IOPin():
  def __init__(self, pin):
    self.pin = pin

  def set_digital_value(self, value):
    send_nores("io.set_digital_value(%s,%d)" % (self.pin, value))

  def get_digital_value(self):
    return send_res_bool("io.get_digital_value(%s)" % self.pin)

  def set_analog_value(self, value):
    send_nores("io.set_analog_value(%s,%d)" % (self.pin, value))

  def get_analog_value(self):
    return send_res_int("io.get_analog_value(%s)" % self.pin)

  def is_touched(self):
    send_res_bool("io.is_touched(%s)" % self.pin)

class IO():
  P0  = IOPin("P0")
  P1  = IOPin("P1")
  P2  = IOPin("P2")
  P3  = IOPin("P3")
  P4  = IOPin("P4")
  P5  = IOPin("P5")
  P6  = IOPin("P6")
  P7  = IOPin("P7")
  P8  = IOPin("P8")
  P9  = IOPin("P9")
  P10 = IOPin("P10")
  P11 = IOPin("P11")
  P12 = IOPin("P12")
  P13 = IOPin("P13")
  P14 = IOPin("P14")
  P15 = IOPin("P15")
  P16 = IOPin("P16")
  P19 = IOPin("P19")
  P20 = IOPin("P20")

io = IO()

def reimport():
  flush()
  send_nores("from microbit import *")
  #prompt()

reimport()
# END
