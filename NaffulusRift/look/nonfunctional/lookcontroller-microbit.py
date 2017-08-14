from microbit import *

def get_sensor_data():
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    a, b = button_a.was_pressed(), button_b.was_pressed()
    print(x, y, z, a, b)

while True:
    sleep(100)
    get_sensor_data()
    display.show("V", wait=False)