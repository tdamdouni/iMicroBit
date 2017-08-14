# This script merely acts to receive messages and relay them to the raspberry pi
from microbit import *
import radio

# radio off by default, must be turned on
radio.on()

# Loop forever, collected data from the controller microbit and relaying to raspberry pi through usb
while True:
  display.scroll("w")
  incoming = radio.receive()
  if incoming:
    display.scroll("r")
    uart.write(incoming + "\n")
