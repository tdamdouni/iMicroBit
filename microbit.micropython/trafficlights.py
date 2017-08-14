# LED Traffic Lights
# Button A causes sequence to run, Button B exits the program.
# Red LED connected to Pin 0
# Yellow LED connected to Pin 1
# Green LED connected to Pin 2

from microbit import *

while True:
    
    pin2.write_digital(1)  # turn on green LED
    
    if button_b.is_pressed():
        # exit program
        break
        
    if button_a.is_pressed():
        # start the light sequence
        sleep(500)
        
        pin2.write_digital(0)  # green LED off
        pin1.write_digital(1)  # yellow LED on
        
        sleep(1000)
        
        pin1.write_digital(0)  # yellow LED off
        pin0.write_digital(1)  # red LED on
        
        # display a count down from 5 to 1
        for i in range(5, 0 , -1):
            display.show(str(i))
            sleep(1000)
        
        display.clear()
        pin1.write_digital(1)  # yellow LED on
         
        sleep(500)
        
        pin1.write_digital(0)  # yellow LED off
        pin0.write_digital(0)  # red LED off
        
pin0.write_digital(0)  # red LED off
pin1.write_digital(0)  # yellow LED off
pin2.write_digital(0)  # green LED off

display.scroll("Goodbye!")