import speech
import microbit

while True:
    if microbit.button_a.was_pressed():
        speech.say('oh my god', pitch=72, speed=84)
        microbit.sleep(100)
        speech.say('its full of stars', pitch=72, speed=84)
