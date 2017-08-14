"""Test MIDI output from micro:bit.

Circuit:

* 3.3V connected to MIDI output socket pin 4 via a 35 ohm resistor
* GND connected to MIDI output socket pin 2
* Pin 0 (TX) connected to MIDI output socket pin 5 via a 10 ohm resistor

"""

import microbit as mb

mb.display.set_pixel(0, 0, 5)
while True:
    if mb.button_a.is_pressed():
        break

    mb.sleep(200)

mb.display.set_pixel(0, 0, 0)
mb.uart.init(baudrate=31250)

while True:
    # send NOTE ON for E above middle C (64) at velocity 100
    mb.uart.write(b'\x90\x40\x64')
    mb.display.set_pixel(0, 0, 5)
    mb.sleep(500)
    mb.display.set_pixel(0, 0, 0)
    mb.uart.write(b'\x80\x40\0')
    mb.sleep(500)
