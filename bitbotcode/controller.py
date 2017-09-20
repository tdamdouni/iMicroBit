# Drive control for the transmitting micro:bit.
from microbit import *
import radio


driver_number = 44  # Lewis Hamilton's number. ;-)
radio.config(channel=driver_number)
radio.on()


# Defines the range of valid tilt from accelerometer readings.
max_tilt = 1000
min_tilt = 199


while True:
    # Grab the inputs.
    y = (accelerometer.get_y() // 200) * 200  # Forwards / backwards.
    x = (accelerometer.get_x() // 200) * 200  # Left / right.
    a = button_a.was_pressed()  # Horn.
    b = button_b.was_pressed()  # Toggle lights.

    # Data from the controller to be sent to the vehicle.
    # [left, right, horn, light]
    control_data = [0, 0, 0, 0]
    if x < -min_tilt and y < -min_tilt:
        # forwards left
        display.show(Image.ARROW_NW)
        control_data[0] = max(y, -max_tilt)
        control_data[1] = max(x, -max_tilt)
    elif x < -min_tilt and y > min_tilt:
        # backwards left
        display.show(Image.ARROW_SW)
        control_data[0] = min(y, max_tilt)
        control_data[1] = max(x, -max_tilt)
    elif x > min_tilt and y < -min_tilt:
        # forwards right
        display.show(Image.ARROW_NE)
        control_data[0] = max(y, -max_tilt)
        control_data[1] = min(x, max_tilt)
    elif x > min_tilt and y > min_tilt:
        # backwards right
        display.show(Image.ARROW_SE)
        control_data[0] = min(y, max_tilt)
        control_data[1] = min(x, max_tilt)
    elif y > min_tilt:
        # backwards
        display.show(Image.ARROW_S)
        control_data[0] = min(y, max_tilt)
    elif y < -min_tilt:
        # forwards
        display.show(Image.ARROW_N)
        control_data[0] = max(y, -max_tilt)
    if a:
        # Sound the horn
        control_data[2] = 1
    if b:
        # Toggle the lights
        control_data[3] = 1
    if not control_data[0]:
        display.clear()
    if any(control_data):
        msg = '{}:{}:{}:{}'.format(*control_data)
        print(msg)
        radio.send(msg)
    sleep(20)
