from microbit import *

while True:
    print(accelerometer.get_x(), accelerometer.get_y(), button_a.is_pressed())
    sleep(100)
    
 