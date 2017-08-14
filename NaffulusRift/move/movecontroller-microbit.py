from microbit import accelerometer, button_a, button_b, display, Image, sleep

deadzone_x = 200
deadzone_y = 200
flag = True


def get_sensor_data():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    print(x, y, z, a, b)
    return x, y


while True:
    sleep(100)
    x, y = get_sensor_data()
    # Display direction output.
    if x < (0 - deadzone_x):
        display.show(Image.ARROW_W, wait=False)
    if x > deadzone_x:
        display.show(Image.ARROW_E, wait=False)
    if y < (0 - deadzone_y):
        display.show(Image.ARROW_N, wait=False)
    if y > deadzone_y:
        display.show(Image.ARROW_S, wait=False)
    if x > (0 - deadzone_x) and x < deadzone_x and y > (0 - deadzone_y) and y < deadzone_y:
        display.show(Image.HAPPY, wait=False)
