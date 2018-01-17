from microbit import *
drop = Image("00900:"
             "09590:"
             "95559:"
             "95559:"
             "09990")
dispenseCount = 0
while True:
    reading = pin0.read_analog()
    if (reading < 800):
        display.show(drop)
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
        sleep(10000)
        dispenseCount += 1
    display.scroll("Water count ")
    display.scroll(str(dispenseCount))