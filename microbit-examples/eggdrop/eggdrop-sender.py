# Eggdrop sender

from microbit import *
# we want to use the radio
import radio


# start the radio, with all default values
radio.on()

# scales the value from one range to another range
def scale(value, minFrom, maxFrom, minTo, maxTo):
    return int((minTo + (maxTo - minTo) * ((value - minFrom) / (maxFrom - minFrom))))

while True:
	# Get accelerometer reading in the X direction
    acc = accelerometer.get_x()
	# scale the reading to fit in the range 0-255
    acc = scale(acc, -1024, 2048, 0, 255)
	# Just to be very sure that the value is not outside the range 0-255.
	# Maybe this should be inside the scale function?
    acc = min(max(acc, 0), 255)
	# Send the value over radio
    radio.send(str(acc))
	# Not sure if this is needed
    sleep(1)
