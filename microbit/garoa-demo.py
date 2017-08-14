from microbit import *
import neopixel
from random import randint

neo = neopixel.NeoPixel(pin0, 16)

scroll_delay = 120
start = -19500
demo = 1
pixel_id = 0

def mensagem(msg):
    demo = 0
    display.scroll(msg, wait = True, delay = scroll_delay)
    start = -19500
    demo = 1

while True:
    # buttons
    if button_a.is_pressed() and button_b.is_pressed():
        demo = 1
    if demo and (running_time() - start) > 19500:
        start = running_time()
        display.scroll("GAROA * HACKERSPACE ITINERANTE * ", wait = False, delay = scroll_delay)
    elif button_a.is_pressed():
        mensagem("OLA")
    elif button_b.is_pressed():
        mensagem("MUNDO")
    # NeoPixel animation
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    neo[pixel_id] = (red, green, blue)
    neo.show()
    sleep(50)
    pixel_id += 1
    if pixel_id >= len(neo):
        pixel_id = 0
