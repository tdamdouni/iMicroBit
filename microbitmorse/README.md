# Morse code text entry for the BBC micro:bit

More a proof of concept than anything, but here's one approach to entering text onto a [BBC micro:bit](https://www.microbit.co.uk/) using nothing more than [Morse code](https://en.wikipedia.org/wiki/Morse_code).

Key in Morse using button A. To get the text displayed, press button B.

At the moment, this only does one word at a time, and the timings are set very slow, as I'm not particularly good at Morse code! Video [demo](https://youtu.be/Kvdbmvlx1Go) of this on YouTube. There's plenty of scope for improvement...

To make the device bleep connect a speaker via pin0 and GND.

This was inspired by, and borrows code from, the [Raspberry Pi Morse code worksheet](https://www.raspberrypi.org/learning/morse-code-virtual-radio/worksheet/).

It was built using [ntoll](https://github.com/ntoll)'s [Mu editor](https://github.com/ntoll/mu) for [BBC micro:bit micropython](https://microbit-micropython.readthedocs.org/en/latest/).

A networked version of this program (connect two BBC micro:bits together with
crocodile clips) is found in the `morse_net.py` script. Instructions and a
[demo](https://www.youtube.com/watch?v=djas6H5wgeM) of this are also on
YouTube. Essentially, pin1 is output and pin2 is input. Connect the output of
one device to the input of the other (and vice versa) then press buttons!
