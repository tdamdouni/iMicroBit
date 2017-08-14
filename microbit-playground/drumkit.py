"""
First attempt at producing noises. I wanted to find out how difficult
it would be to implement a basic "sample" sequencer (think drum-kit).

Current version repeats the same pre-defined pattern.

Scrolling (or any kind of) UI would be nice...
"""

import microbit
import music

# Frequencies for octave 4
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.0
B4 = 493.88


def fx(length_ms, pitch, delta_pitch, steps_count):
    """Produce sound effect shifting pitch by delta_pitch in steps_count steps"""
    end_time = round(microbit.running_time() + length_ms)

    step_length_ms = round(length_ms/steps_count)

    while microbit.running_time() < end_time:
        if pitch > 0:
            music.pitch(round(pitch))
        microbit.sleep(step_length_ms)

        pitch += delta_pitch
        steps_count -= 1

    music.stop()


def noise(length_ms):
    """Random noise"""

    end_time = round(microbit.running_time() + length_ms)

    while microbit.running_time() < end_time:
        microbit.pin0.write_digital(microbit.random(2))

    music.stop()


def show(what):
    """One day this can drive disco-lights"""
    microbit.display.show(what)


# drums
fx_boing = lambda length_ms: (show("+"), fx(length_ms, C4/2, -10, 15))
fx_ksch  = lambda length_ms: (show("#"), fx(length_ms, C4*4, -100, 5))
fx_noise = lambda length_ms: (show("*"), noise(length_ms))
fx_click = lambda length_ms: (show("8"), fx(length_ms, 4186.01, +100, 15))

# 2*8 beats
pattern = [fx_boing, fx_click, fx_boing, None, fx_noise, None, fx_boing, fx_boing,
           fx_click, fx_ksch,  fx_boing, None, fx_noise, None, fx_ksch,  None,
          ]

# main loop
while True:
    for f in pattern:
        if f is None:
            microbit.sleep(100)
        else:
            f(50)
            microbit.sleep(50)
