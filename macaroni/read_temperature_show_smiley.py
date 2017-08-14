import microbit

""" Script that shows the temperature and then a happy/sad
    face depending on the temperature.
"""

while True:
    sensor_val = microbit.pin0.read_analog()
    voltage = (sensor_val / 1024) * 3000
    temperature = (voltage - 500)/10
    microbit.display.scroll("%.1f" % float(temperature), 200)

    if temperature > 5.0:
        face=microbit.Image.HAPPY
    else:
        face=microbit.Image.SAD

    microbit.display.show(face)
    microbit.sleep(5000)
