"""Play the builtin tunes via MIDI.

MIDI output circuit:

https://www.midi.org/articles/midi-electrical-specifications

1. 3.3V connected to MIDI output socket pin 4 via a 35 ohm resistor
2. GND connected to MIDI output socket pin 2
3. Pin 0 (TX) connected to MIDI output socket pin 5 via a 10 ohm resistor

"""

# -----------------------------------------------------------------------------
# START OF MIDI LIBRARY CODE

# global constants
NOTE_OFF = 0x80
NOTE_ON = 0x90
CONTROLLER_CHANGE = 0xB0
PROGRAM_CHANGE = 0xC0


class MidiOut:
    def __init__(self, device=None, channel=1):
        if not hasattr(device, 'write'):
            raise TypeError("device instance must have a 'write' method.")
        if channel < 1 or channel > 16:
            raise ValueError('channel must be an integer between 1..16.')
        self.channel = channel
        self.device = device
    def channel_message(self, command, *data, ch=None):
        command = (command & 0xf0) | ((ch if ch else self.channel) - 1 & 0xf)
        msg = [command] + [value & 0x7f for value in data]
        self.device.write(bytes(msg))
    def note_off(self, note, velocity=0, ch=None):
        self.channel_message(NOTE_OFF, note, velocity, ch=ch)
    def note_on(self, note, velocity=127, ch=None):
        self.channel_message(NOTE_ON, note, velocity, ch=ch)
    def control_change(self, control, value, lsb=False, ch=None):
        self.channel_message(CONTROLLER_CHANGE, control,
                             value >> 7 if lsb else value, ch=ch)
        if lsb and control < 20:
            self.channel_message(CONTROLLER_CHANGE, control + 32, value, ch=ch)
    def program_change(self, program, ch=None):
        self.channel_message(PROGRAM_CHANGE, program, ch=ch)

# END OF MIDI LIBRARY CODE
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Main script

import music
from microbit import button_a, button_b, display, sleep, uart


TUNES = ['DADADADUM', 'ENTERTAINER', 'PRELUDE', 'ODE', 'NYAN', 'RINGTONE',
    'FUNK', 'BLUES', 'BIRTHDAY', 'WEDDING', 'FUNERAL', 'PUNCHLINE', 'PYTHON',
    'BADDY', 'CHASE', 'WAWAWAWAA', 'JUMP_UP', 'JUMP_DOWN', 'POWER_UP',
    'POWER_DOWN']

PROGRAMS = [
    0,   # Grand Piano
    49,  # String Esemble
    25,  # Acoustic Guitar
    35,  # Picked Electric Bass
    10,  # Glockenspiel
]

NOTES = {
    'c': 0,
    'd': 2,
    'e': 4,
    'f': 5,
    'g': 7,
    'a': 9,
    'b': 11,
}


def play(midi, notes):
    led = 0
    duration = octave = 4
    bpm, ticks = music.get_tempo()
    mpt = 60000 / bpm / ticks

    try:
        for note in notes:
            try:
                note, duration = note.split(':')
                duration = int(duration)
            except:
                pass

            try:
                octave = int(note[-1])
                note = note[:-1]
            except (ValueError, IndexError):
                pass

            note = note.lower()
            midinote = NOTES.get(note[0])

            if midinote is not None:
                if note.endswith('#'):
                    midinote += 1
                elif len(note) > 1 and note.endswith('b'):
                    midinote -= 1

                midinote = max(0, min(127, midinote + 12 * octave))
                midi.note_on(midinote, 96)
                display.set_pixel(led, 0, 5)

            sleep(duration * mpt)

            if midinote is not None:
                midi.note_off(midinote)
                display.set_pixel(led, 0, 0)
                led = (led+1) % 5

        # make sure led and last note is turned off
        if midinote is not None:
            display.set_pixel(led, 0, 0)
            midi.note_off(midinote)
    except:
        # Send all sound off to prevent hanging notes
        midi.control_change(0x78, 0)


# wait for button A press before initializing the UART
# to allow uploading of new firmware
while True:
    if button_a.is_pressed():
        display.set_pixel(0, 0, 0)
        break

    display.set_pixel(0, 0, 5)
    sleep(100)
    display.set_pixel(0, 0, 0)
    sleep(100)

# Initialize UART for MIDI
uart.init(baudrate=31250)
midi = MidiOut(uart)

tune = program = 0
# send a PROGRAM CHANGE to set instrument to #0 (Grand Piano)
midi.program_change(program)
# set led on first 4 rows of display to indicate current tune (1-20)
display.set_pixel(program, 4, 5)
# set led on lowest row of display to indicate selected program (1-5)
display.set_pixel(program, 4, 5)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # when both buttons are pressed, change to next program (instrument)
        display.set_pixel(program, 4, 0)
        program = (program+1) % len(PROGRAMS)
        display.set_pixel(program, 4, 5)
        midi.program_change(PROGRAMS[program])
    elif button_a.is_pressed():
        # When button A is pressed, play the current tune
        play(midi, getattr(music, TUNES[tune]))
        display.set_pixel(tune % 5, int(tune / 5), 5)
    elif button_b.is_pressed():
        # When button B is pressed, select the next of the builtin tunes
        display.set_pixel(tune % 5, int(tune / 5), 0)
        tune = (tune+1) % len(TUNES)
        display.set_pixel(tune % 5, int(tune / 5), 5)

    sleep(200)
