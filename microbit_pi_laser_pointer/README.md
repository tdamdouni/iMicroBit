# microbit_pi_laser_pointer
Project using the microbit to send messages to raspberry pi, which will in turn move a laser pointer

## Hardware Requirements
```
1 raspberry pi
2 microbits
Turret containing two servos (build directions and pictures forthcoming)
6 volts power supply for the servos, 4 AA batteries will do(do not power servos through Pi directly)
```

## Languages Used

Everything is written in Python.

## Plugging in Your Servos

## How it works
1 microbit will be connected directly to the raspberry pi and act in the capacity of an information hub.  The other microbit will be powered by battery and will be used to control motion of the laser pointer using the onboard accelerometer.

So flow is as follows:
1. each of the devices are turned on. Plug the "hub" microbit into the Raspberry Pi USB port.  Plug in servos before turning on the Raspberry Pi.
2. The controller waits for the user to press "a" or "b".  If the user presses "a", a single set of coordinates will be sent to the hub microbit using radio; if "b" is pressed, the microbit will stream data until "b" is pressed again.  Anytime the controller microbit sends, the letters "se" appear on the leds.  The values that are sent are "x" and "y" tilt values, which range from -1000 to +1000.
3.  The hub microbit receives incoming data from the controller microbit.  This data is then sent directly to the Raspberry Pi through a USB connection.  If the hub is currently waiting for input, "w" is printed to the leds.  If it has input, "r" is written to the leds.
4.  The Raspberry Pi will parse the incoming data and convert the data to values that are acceptable to our servos.  The servos will then be moved to the location suggested by the coordinates.  The console will also print out the current servo-converted-values of x and y.

This project was a proof of the following concepts: radio reliability,  accuracy of the microbit's accelerometer, and live communication between the microbit and external devices via usb.  The project was a success with zero hiccups, the microbit seems very reliable in its data communications and sensor accuracy.
