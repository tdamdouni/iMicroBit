# NON-WORKING
#
# Requires PyAutoGUI
# See https://pyautogui.readthedocs.io/en/latest/install.html
# for install docs.

import serial
from time import sleep
import pyautogui

def move ():	
    deadzone_x = 200
    deadzone_y = 200
    key_delay = 0.4
        
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
            if int(x) < (0 - deadzone_x) :
                print("A generated")
                pyautogui.typewrite('aaaaa') # This works, but barely
                pyautogui.keydown('a')
                time.sleep(key_delay)
                pyautogui.keyup('a')
            if int(x) > deadzone_x:
                print("D generated")
                pyautogui.keydown('d')
                time.sleep(key_delay)
                pyautogui.keyup('d')
            if int(y) < (0 - deadzone_y):
                print("W generated")
                pyautogui.keydown('w')
                time.sleep(key_delay)
                pyautogui.keyup('w')
            if int(y) > deadzone_y:
                print("S generated")
                pyautogui.keydown('s')
                time.sleep(key_delay)
                pyautogui.keyup('s')
            #~ else:
                #~ pyautogui.keyup('a')
                #~ pyautogui.keyup('d')
                #~ pyautogui.keyup('w')
                #~ pyautogui.keyup('s')
            #~ print(x, y, z, a, b)
        
        except:
            pass
        
    s.close()
    
    
if __name__ == "__main__":
    move()
