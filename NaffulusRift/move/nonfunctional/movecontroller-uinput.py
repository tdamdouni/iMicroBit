# NON-WORKING
#
# Requires `sudo apt-get install libudev-dev`
# Then:
# `sudo pip3 install python-uinput`
# &:
# `sudo modprobe uinput`
# Code heavily based on https://www.raspberrypi.org/learning/microbit-game-controller/worksheet/

# Doesn't actually work - Correctly receives data and emits keyboard events, but
# Minecraft stubbornly ignores input via uinput. Harrumph.


import serial
from time import sleep
import uinput

def move ():	
	deadzone_x = 200
	deadzone_y = 200
	
	device = uinput.Device([
		uinput.KEY_W,
		uinput.KEY_S,
		uinput.KEY_A,
		uinput.KEY_D] )
		
	PORT = "/dev/ttyACM0"
	#~ PORT = "/dev/serial/by-id/usb-MBED_MBED_CMSIS-DAP_9900023431864e45001210060000003700000000cc4d28bd-if01"
	BAUD = 115200
	
	s = serial.Serial(PORT)
	s.baudrate = BAUD
	s.parity = serial.PARITY_NONE
	s.databits = serial.EIGHTBITS
	s.stopbits = serial.STOPBITS_ONE
	
	while True:
		data = s.readline().decode('UTF-8')
		data_list = data.rstrip().split(' ')
		try:
			x, y, z, a, b = data_list
			if int(x) < (0 - deadzone_x) :
				#print("a")
				device.emit_click(uinput.KEY_A)
			if int(x) > deadzone_x:
				#print("d")
				device.emit_click(uinput.KEY_D)
			if int(y) < (0 - deadzone_y):
				#print("w")
				device.emit_click(uinput.KEY_W)
			if int(y) > deadzone_y:
				#print("s")
				device.emit_click(uinput.KEY_S)
			
			#~ print(x, y, z, a, b)
		
		except:
			pass
		
	s.close()
	
	
if __name__ == "__main__":
	move()
