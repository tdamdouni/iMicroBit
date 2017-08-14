# Add your Python code here. E.g.
from microbit import *
import radio

speed_off = 0
speed_rotate_slow = 128
speed_rotate_fast = 256
speed_hook_slow = 160
speed_hook_fast = 256

radio.on()
radio.config(channel=7, group=42)

x = 2
y = 2

pin0.write_analog(speed_off)
pin8.write_analog(speed_off)
pin12.write_analog(speed_off)
pin16.write_analog(speed_off)

sleep_time = 250
pulse_low = 4
pulse = pulse_low

while True:
    display.clear()
    
    recv_string = radio.receive()
    if recv_string != None:
        # PXT radio sends device serial number at beginning of string
        # so we need to strip all but last 2 characters
        try:
            if len(recv_string) > 2:
                recv_string = recv_string[-2:]
            recv_int = int(recv_string)
            x = recv_int // 10
            y = recv_int % 10
        except:
            # Handle any exception from above
            x = 2
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

    # Rotation
    if x > 3:
        pin16.write_analog(speed_rotate_fast)
        pin0.write_analog(speed_off)
    elif x > 2:
        pin16.write_analog(speed_rotate_slow)
        pin0.write_analog(speed_off)
    elif x < 1:
        pin16.write_analog(speed_off)
        pin0.write_analog(speed_rotate_fast)
    elif x < 2:
        pin16.write_analog(speed_off)
        pin0.write_analog(speed_rotate_slow)
    else:
        pin16.write_analog(speed_off)
        pin0.write_analog(speed_off)

    # Hook
    if y > 3:
        pin8.write_analog(speed_hook_fast)
        pin12.write_analog(speed_off)
    elif y > 2:
        pin8.write_analog(speed_hook_slow)
        pin12.write_analog(speed_off)
    elif y < 1:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_hook_fast)
    elif y < 2:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_hook_slow)
    else:
        pin8.write_analog(speed_off)
        pin12.write_analog(speed_off)
    
    sleep(sleep_time)
