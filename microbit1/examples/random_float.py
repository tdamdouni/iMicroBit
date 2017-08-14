import random

from microbit import display

answer = random.randrange(100) + random.random()
display.scroll(str(answer))
