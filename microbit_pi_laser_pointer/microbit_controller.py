# code to be placed on the battery powered microbit controller
from microbit import *
import radio

# my_switch variable will control our b button while loop
my_switch = False

# By default radio is off to conserve electricity, must turn on
radio.on()

# Send accelerometer data to the hub microbit
def send_acc_data():
    my_send = accelerometer.get_values()                # Get acc data
    radio.send(str(my_send[0])+"," + str(my_send[1]))   # Send only x and y data as comma separated string
    sleep(800)    

# Loop forever, check for button presses, send data accordingly
# A button will trigger a single data send, b button sets switch and activates a new loop to consistently send data
# The switch variable controls the b button while loop.  When true loop is executed, if false its not
while True:
    if button_a.was_pressed():
        send_acc_data()
    if button_b.was_pressed():
        my_switch = True
        while my_switch:
            send_acc_data()
            if button_b.was_pressed():
                my_switch = False
  
