"""Morse code game.

Try guessing the morse code for the character displayed on the screen.
Use short (less than 250ms) or long (more than 250ms) presses on the A button,
then press the B button when you're done.

If you guessed correctly, you'll see a "ok mark", otherwise you'll be greeted
with a big cross, and the correct code will be displayed.
"""
import random
from microbit import *

MORSE_CODE_LOOKUP = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

DOT = Image('00000:'
            '00000:'
            '00900:'
            '00000:'
            '00000:')


DASH = Image('00000:'
             '00000:'
             '09990:'
             '00000:'
             '00000:')


def check_answer(letter, answer):
    """Make sure the given answer corresponds to the letter expected."""
    return MORSE_CODE_LOOKUP[letter] == answer


def wait_for_a_press():
    """Return a dot or a dash for the time the button A has been pressed."""
    a_pressed = button_a.was_pressed()
    b_pressed = button_b.was_pressed()
    while not a_pressed and not b_pressed:
        a_pressed = button_a.was_pressed()
        b_pressed = button_b.was_pressed()

    if b_pressed:  # End of the answer.
        return

    start_press = running_time()
    while button_a.is_pressed():
        pass
    time_pressed = running_time() - start_press

    if time_pressed < 250:
        display.show(DOT)
        return '.'
    else:
        display.show(DASH)
        return '-'


while True:
    answer = []
    letter = random.choice(tuple(MORSE_CODE_LOOKUP.keys()))
    display.show(letter)
    press = wait_for_a_press()
    while press:  # Wait for the full answer.
        answer.append(press)
        press = wait_for_a_press()

    if check_answer(letter, ''.join(answer)):
        display.show(Image.YES)
        sleep(1000)
    else:
        display.show(Image.NO)
        sleep(1000)
        display.scroll(MORSE_CODE_LOOKUP[letter])
