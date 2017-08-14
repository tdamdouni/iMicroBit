import microbit

if not microbit.compass.is_calibrated():
    microbit.compass.calibrate()

if microbit.compass.is_calibrated():
    microbit.display.show(microbit.Image.HAPPY)
else:
    microbit.display.show(microbit.Image.SAD)

microbit.sleep(1000)

while True:
    angle = microbit.compass.heading()
    point = int((360 - angle) / 30)
    microbit.display.show(microbit.Image.ALL_CLOCKS[point])
    microbit.sleep(100)
