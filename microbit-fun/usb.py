"""USB: read messages sent from the computer connected via USB (serial).

Messages sent to the micro:bit using the pyserial python library on the
computer will be displayed.

An easy way to connect to the micro:bit serial port on the computer is to start
a REPL (using `python`), then:
>>> import microfs
>>> s = microfs.get_serial()
>>> s.write("Hello world")
"""
from microbit import *


uart.init(baudrate=115200)
while True:
    line = uart.readline()
    if line:
        display.scroll(line)
