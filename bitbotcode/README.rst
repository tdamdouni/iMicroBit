bitbotcode
----------

The driver and controller code for radio controlled bit:bot robots.

What is a bit:bot..? See: http://4tronix.co.uk/bitbot/

Due to a bug in the current runtime, the "horn" feature doesn't work (and is
thus commented out). I'll update this code when a new version of the
runtime is released.

See the following video for a demo:

https://www.youtube.com/watch?v=e0dh-eH8J3I

The code is copiously commented. The more you tilt the controller the more
speed / turn is applied by the driver.

Customise
=========

To use more than one bot at once you must make sure each controller/driver
pair have a unique ``driver_number``. You should also change the driver's
logo and colour.
