# Add your Python code here. E.g.
from microbit import *
import neopixel


np = neopixel.NeoPixel(pin13, 12)

rainbow_raw = [
    (255, 0, 0),
    (255, 127, 0),
    (255, 255, 0),
    (127, 255, 0),
    (0, 255, 0),
    (0, 255, 127),
    (0, 255, 255),
    (0, 127, 255),
    (0, 0, 255),
    (127, 0, 255),
    (255, 0, 255),
    (255, 0, 127),
]

dim = lambda r, g, b: (r//20, g//20, b//20)

rainbow = [dim(*c) for c in rainbow_raw]

shift = 0
while True:
    for i in range(6):
        np[i] = rainbow[(i + shift) % len(rainbow)]
        np[i+6] = rainbow[(i + shift) % len(rainbow)]
        np.show()

    if abs(accelerometer.get_y()) >= 90:
        shift += 1 if accelerometer.get_y() > 0 else -1
        shift %= len(rainbow)

    sleep(100)
