# acc.py  20/11/2016  D.J.Whale
#
# Send accelerometer readings via the USB serial port

from microbit import *

DELAY_MS = 100

def run():
    while True:
        x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
        print(x,y,z)
        sleep(DELAY_MS)
    
run()

