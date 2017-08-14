# mb_remote
A simple way to 'remote' control a micro:bit from Python on a PC/Mac/Pi/Linux

This was some work that I did in August 2015 when MicroPython was first ported to the micro:bit

In it's current state it is now out of step with the MicroPython API, but the concept is sound and it could easily be developed into a working solution again.

The way I did this was to create a microbit module that you import on the
PC/mac/pi/linux like this

import microbit

And then for each micro:bit feature, the PC version would send the
appropriate REPL to MicroPython running on the micro:bit, it would 'do it's
stuff' and return the result.

So, writing this on the PC

import microbit
import time

    while True:
        x = microbit.accelerometer.get_x()
        y = microbit.accelerometer.get_y()
        print("pos %s %s" % (x, y))
        time.sleep(1)

The bulk of this loop runs on the existing installed python on the PC. When
it calls microbit.accelerometer.get_x() it sends a message to the micro:bit
REPL to get the x acceleration, it returns the value, and that is assigned
to the x variable in the python running on the PC.

So, the micro:bit just becomes a sort of remote sensing device.

    microbit.display.scroll("hello world")

Running this on the PC would scroll Hello World on the micro:bit display.


TODO LIST
----

The micro:bit MicroPython API has changed quite a lot since I first wrote
this, but if this is what you are talking about, I could upload the code to
github and someone else could help me update it to the latest API :)

It probably only works with python 2 at the moment and will need some love
to make it python 3 compatible.




CONTRIBUTIONS
----

Note that a version of pyserial is embedded inside this project, as allowed
by the licence agreement from pyserial. This is so that you don't have to
install any dependent packages. The microbit.py module can be configured
to use the embedded pyserial or the installed one in the dist path by 
changing a flag in the file.

pyserial 2.7 (python licence) comes from here:

https://github.com/pyserial/pyserial


The anyio package is something I wrote to make it possible to use an Arduino 
on PC/Mac/Linux to simulate the Raspberry Pi RPi.GPIO features, to allow
GPIO projects to be written that work on any platform.

anyio (MIT licence) comes from here:

https://github.com/whaleygeek/anyio


