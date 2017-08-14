from microbit import *
import radio

radio.on()
radio.config(channel=86)
sleep_time = 190


def output(data):
    data = str(data)
    if len(data) == 1:
        display.show(data)
    else:
        display.scroll(data)

def inc_letter(c):
    output(ALPHA[c])
    c += 1
    if c == len(ALPHA):
        c = 0
    return c
    
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
msg = ""

c = 0
while True:
    if button_a.is_pressed():
        c = inc_letter(c)
    elif button_b.is_pressed():
        if ALPHA[c-1] == "_":
            msg += " "
        else:
            msg += ALPHA[c-1]
        c = 0
        output(" ")
        sleep(sleep_time)
        while True:
            if button_b.is_pressed():
                radio.send(msg)
                msg = ""
                break
            elif button_a.is_pressed():
                c = inc_letter(c)
                break
    
    sleep(sleep_time)
        
