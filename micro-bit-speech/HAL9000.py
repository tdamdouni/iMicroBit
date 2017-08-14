from microbit import *
from microbit import random
import speech

answers = [
    "Affirmative, I read you, YOUR NAME",
    "I'm sorry, YOUR NAME",
    "I'm afraid, I can't do that",
    "I know that you were planning to disconnect me",
    "I'm afraid that's something I cannot allow to happen",
    "Without your space helmet you are going to find it rather difficult",
    "YOUR NAME, this conversation can serve no purpose anymore",
    "Goodbye",
]
while True:
    display.scroll("HAL 9000")
if button_a.is_pressed:
    display.clear()
    sleep(1000)
    speech.say(random.choice(answers), speed=90, pitch=85, throat=100, mouth=190)
