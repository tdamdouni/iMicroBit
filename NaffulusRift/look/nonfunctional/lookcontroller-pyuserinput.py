# PyUserInput test.
# Requires sudo pip3 install pyuserinput python3-xlib
#
# Code heavily based on https://www.raspberrypi.org/learning/microbit-game-controller/worksheet/
# Non-working; can't get PyUserInput mouse module to do anything on Raspbian.


import serial
from time import sleep
from pymouse import PyMouse

def move ():
    deadzone_x = 200
    deadzone_y = 200
    key_delay = 0.4
    
    mouse = PyMouse()
    
    PORT = "/dev/ttyACM1"
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
            x_mapped = arduino_map(int(x), -1024, 1024, -960, 960)
            y_mapped = arduino_map(int(y), -1024, 1024, -540, 540)
            
            x_centre = 960
            y_centre = 540
        
            print(x_mapped, y_mapped)
            mouse.move(x_centre + x_mapped, y_centre + y_mapped)
        
        except:
            pass
        
    s.close()
    
    
if __name__ == "__main__":
    move()
