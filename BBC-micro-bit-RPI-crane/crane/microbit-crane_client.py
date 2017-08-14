# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
radio.config(channel=7, group=42)

threshold1 = 400
threshold2 = 800

sleep_time = 500
pulse_low = 4
pulse = pulse_low

prev_x = 5
prev_y = 5

while True:
    acc_x = accelerometer.get_x()
    acc_y = accelerometer.get_y()
    
    display.clear()
    
    if acc_x > threshold2:
        x = 4
    elif acc_x > threshold1:
        x = 3
    elif acc_x < -threshold2:
        x = 0
    elif acc_x < -threshold1:
        x = 1
    else:
        x = 2

    if acc_y > threshold2:
        y = 4
    elif acc_y > threshold1:
        y = 3
    elif acc_y < -threshold2:
        y = 0
    elif acc_y < -threshold1:
        y = 1
    else:
        y = 2

    if x == 2 and y == 2:
        if pulse == 9:
            delta = -1
        elif pulse == pulse_low:
            delta = 1
        pulse = pulse + delta
        display.set_pixel(x, y, pulse)
    else:
        display.set_pixel(x, y, 9)
    
    if x != prev_x or y != prev_y:
        send_string = str(x) + str(y)
        radio.send(send_string)

        prev_x = x
        prev_y = y
    
    sleep(sleep_time)
