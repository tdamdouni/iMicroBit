#written by Thomas Stratford inspired by Nicholas Tollervey.
#Basic Radio instructions taken from https://microbit-micropython.readthedocs.io/en/latest/tutorials/radio.html


from microbit import *
import radio
import neopixel
np = neopixel.NeoPixel(pin0, 1)

green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 153, 0)

radio.on()
while True:
    # Read any incoming messages.
    message = radio.receive()
    if message:
        np[0] = (green)
        np.show()
        display.show(Image.DUCK)
        sleep(3000)
        np.clear()
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        np [0] = (red)
        np.show()
        sleep(1000)
        np [0] = (orange)
        np.show()
        sleep(1000)
        np.clear()
        display.clear()
        radio.send("hello")
        