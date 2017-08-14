"""
Simple script to display sensor values on terminal.

Use something like this to run it (requires wide terminal):

  pyboard.py /dev/ttyACM0 read-sensors.py
"""

from microbit import *

def print_array(prefix, array, end="\n"):
    fmt = "{:>7}|" * len(array)
    print(prefix, fmt.format(*array), end=end)


# discover pins
analog_pins = []
digital_pins = []
touch_pins = []

pin_digital_heading = ""
pin_analog_heading = ""
pin_touch_heading = ""

# only include pins 0-2. Other pins can be specified (or None to skip) if
# needed.
for i, pin in enumerate([pin0, pin1, pin2]):
    if pin is not None:
        pin_str = " pin{:<2}".format(i)

        # check read_analog
        try:
            pin.read_analog
            analog_pins.append(pin)
            pin_analog_heading += pin_str + "a|"
        except AttributeError:
            pass

        # check read_digital
        try:
            pin.read_digital
            digital_pins.append(pin)
            pin_digital_heading += pin_str + "d|"
        except AttributeError:
            pass

        # check is_touched
        try:
            pin.is_touched
            touch_pins.append(pin)
            pin_touch_heading += pin_str + "t|"
        except AttributeError:
            pass


# calibrate the compass
compass.calibrate()
print("Calibrating compass. Please spin the micro:bit. 'comp_c' becomes 1 once "
      "micro:bit has been calibrated.\n")

# main loop
while True:

    min_array, max_array = None, None

    print("     "
          "  acc_x|"
          "  acc_y|"
          "  acc_z|"
          "  btn_a|"
          "  btn_b|"
          " comp_c|"
          " comp_x|"
          " comp_y|"
          " comp_z|"
          " comp_h|"
          + pin_analog_heading
          + pin_digital_heading
          + pin_touch_heading
         )

    # 100 samples per batch
    for _ in range(100):

        # collect sensor values into array
        array = []
        array.extend(accelerometer.get_values())

        array.append(button_a.is_pressed())
        array.append(button_b.is_pressed())

        array.append(compass.is_calibrated())
        array.append(compass.get_x())
        array.append(compass.get_y())
        array.append(compass.get_z())
        array.append(compass.heading())

        for pin in analog_pins:
            array.append(pin.read_analog())

        for pin in digital_pins:
            array.append(pin.read_digital())

        for pin in touch_pins:
            array.append(pin.is_touched())

        # update min_array, max_array
        if min_array is None:
            min_array, max_array = array, array
        else:
            min_array = [min(v) for v in zip(min_array, array)]
            max_array = [max(v) for v in zip(max_array, array)]

        # print current and wait
        print_array("    ", array, end="\r")
        sleep(50)

    # print min/max values for last batch
    print_array("min:", min_array)
    print_array("max:", max_array)
    print()
