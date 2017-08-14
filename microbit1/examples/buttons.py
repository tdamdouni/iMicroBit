from microbit import display, Image
from microbit import sleep, button_a


def set_leds(level: int):
    """Set all LEDs level to equal value."""
    display.show(Image('{0}:{0}:{0}:{0}:{0}'.format(str(level) * 5)))


def blink():
    """Blink by all LEDs"""
    display.clear()
    sleep(500)
    set_leds(9)
    sleep(500)
    display.clear()


blink()
sleep(10000)
display.scroll(str(button_a.get_presses()))  # Number of presses
