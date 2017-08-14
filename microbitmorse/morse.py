from microbit import *
import music


# A lookup table of morse codes and associated characters.
MORSE_CODE_LOOKUP = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}


def decode(buffer):
    # Attempts to get the buffer of Morse code data from the lookup table. If
    # it's not there, just return a full stop.
    return MORSE_CODE_LOOKUP.get(buffer, '.')


# How to display a single dot.
DOT = Image("00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000:")


# How to display a single dash.
DASH = Image("00000:"
             "00000:"
             "09990:"
             "00000:"
             "00000:")


# To create a DOT you need to hold the button for less than 250ms.
DOT_THRESHOLD = 250
# To create a DASH you need to hold the button for less than 500ms.
DASH_THRESHOLD = 500


# Holds the incoming Morse characters.
buffer = ''
# Holds the translated Morse as normal text.
message = ''
# The time from which the device has been waiting for the next keypress.
started_to_wait = running_time()


# Put the device in a loop to wait for and react to key presses.
while True:
    # Work out how long the device has been waiting for a keypress.
    waiting = running_time() - started_to_wait
    # Reset the timestamp for the key_down_time.
    key_down_time = None
    # If button_a is held down, then...
    while button_a.is_pressed():
        # Play a beep - this is Morse code y'know ;-)
        music.pitch(880, 10)
        # ...and if there's not a key_down_time then set it to now!
        if not key_down_time:
            key_down_time = running_time()
    # Get the current time and call it key_up_time.
    key_up_time = running_time()
    # If there's a key_down_time (created when button_a was first pressed
    # down).
    if key_down_time:
        # ... then work out for how long it was pressed.
        duration = key_up_time - key_down_time
        # If the duration is less than the max length for a "dot" press...
        if duration < DOT_THRESHOLD:
            # ... then add a dot to the BUFFER containing incoming Morse codes
            # and display a dot on the display.
            buffer += '.'
            display.show(DOT)
        # Else, if the duration is less than the max length for a "dash"
        # press... (but longer than that for a DOT ~ handled above)
        elif duration < DASH_THRESHOLD:
            # ... then add a dash to the BUFFER and display a dash.
            buffer += '-'
            display.show(DASH)
        # Otherwise, any other sort of keypress duration is ignored (this isn't
        # needed, but added for "understandability").
        else:
            pass
        # The button press has been handled, so reset the time from which the
        # device is starting to wait for a  button press.
        started_to_wait = running_time()
    # Otherwise, there hasn't been a button_a press during this cycle of the
    # loop, so # check there's not been a pause to indicate an end of the
    # incoming Morse code character. The pause must be longer than a DASH
    # code's duration.
    elif len(buffer) > 0 and waiting > DASH_THRESHOLD:
        # There is a buffer and it's reached the end of a code so...
        display.clear()
        # Decode the incoming buffer.
        character = decode(buffer)
        # Reset the buffer to empty.
        buffer = ''
        # Show the decoded character.
        display.show(character)
        # Add the character to the message.
        message += character
    # Finally, if button_b was pressed while all the above was going on...
    if button_b.was_pressed():
        # ... display the message,
        display.scroll(message)
        # then reset it to empty (ready for a new message).
        message = ''
