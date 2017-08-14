from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        answers = [Image.YES, Image.NO, Image.MEH]
        answer = random.choice(answers)
        display.show(answer)
        sleep(3000)
        display.clear()
