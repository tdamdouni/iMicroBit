# Eggdrop receiver


from microbit import *

# we want to use the radio
import radio

# start the communication over usb, with baudrate 115200
# make sure you set the same baudrate on the other end of this communication
uart.init(115200)

# start the radio, with all settings to default
radio.on()

# a bytearray with a linefeed character
buffer = bytearray(1)
buffer[0] = 10

while True:
    try:
		# receive a string over radio
        input = radio.receive()
        if input is not None:
			# write the string to the USB communication
            uart.write(input)
            # also write a linefeed character
            uart.write(buffer)
        else:
			# if we didn't receive anything show an F on the display
            display.scroll("F", 80)
    except ValueError:
		# Not sure why this happens, but sometimes the received information throws this error
		# Restarting the radio seems to be needed
        input = None
        radio.reset()
        radio.off()
        radio.on()
	# a short pause
    sleep(10)
