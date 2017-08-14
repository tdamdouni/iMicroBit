from microbit import display, pin0, pin1, pin2

while True:
    if pin0.is_touched():
        display.show('0')
    elif pin1.is_touched():
        display.show('1')
    elif pin2.is_touched():
        display.show('2')
    else:
        display.clear()
