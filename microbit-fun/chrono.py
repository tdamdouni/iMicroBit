"""Chrono.

Nothing to do but to read the time elapsed since the demo has been started, in
the HH:MM:SS format.
"""
from microbit import *
from utils import NUMBERS, image_from_number, zigzag


def get_time_elapsed(start):
    """Return the time elapsed since start, formatted as HH:MM:SS."""
    seconds = (running_time() - start) // 1000
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{hours:02}:{minutes:02}:{seconds:02}".format(
        seconds=seconds, minutes=minutes, hours=hours)


start = running_time()
while True:
    def get_time_to_display():
        seconds = (running_time() - start) // 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        formatted = "{hours:02}:{minutes:02}:{seconds:02}".format(
            seconds=seconds, minutes=minutes, hours=hours)
        return image_from_number(formatted)
    zigzag(get_time_to_display, 30, 300)
