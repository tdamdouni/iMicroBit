import random
import os
import speech

from microbit import *

if 'messages.txt' in os.listdir():

    with open('messages.txt') as message_file:
        messages = message_file.read().split('\n')

    while True:
        if button_a.was_pressed():
            speech.say(random.choice(messages))
