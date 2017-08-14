#!/usr/bin/env python
"""Test play() function withmock Midi object."""

import time


NOTES = {
    'c': 0,
    'd': 2,
    'e': 4,
    'f': 5,
    'g': 7,
    'a': 9,
    'b': 11,
}


def sleep(s):
    print("... sleeping %s ms" % s)
    time.sleep(s / 1000.)


class MockMidi:
    def note_on(self, *args, **kw):
        print("note on:", *args)
    def note_off(self, *args, **kw):
        print("note off:", *args)
    def control_change(self, *args, **kw):
        print("cc:", *args)


def play(midi, notes):
    duration = octave = 4
    #bpm, ticks = music.get_tempo()
    bpm, ticks = 120, 4
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

            sleep(duration * mpt)

            if midinote is not None:
                midi.note_off(midinote)
    except:
        # Send all sound off to prevent hanging notes
        midi.control_change(0x78, 0)
        raise


tune = ('r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8')
play(MockMidi(), tune)
