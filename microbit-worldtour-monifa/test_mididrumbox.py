import sys

from rtmidi.midiutil import open_midioutput

from midiout import MidiOut
from drumseq import Pattern, Sequencer


# hack to substitute rtmidi.MidiOut for uart
class RtMidiOut:
    def __init__(self, midi):
        self.midi = midi
    def write(self, msg):
        self.midi.send_message(msg)


def _test():
    ROSANNA = """
    # Rosanna Shuffle
    # about 124 bpm (for a real tempo of 93 bpm)
    #  1..|..|..|..2..|..|..|..
    36 x....m...x.....m..s..... Bassdrum
    40 .+-.+-m+-.+-.+-.+-m+-.++ Snare 2
    42 x-sx-sx-sx-sx-sx-sx-sx-s Closed Hi-hat
    """

    midi, _ = open_midioutput(sys.argv[1] if len(sys.argv) > 1 else None,
        client_name="drumseq", port_name="MIDI Out")
    midi = MidiOut(RtMidiOut(midi))
    seq = Sequencer(midi, bpm=124)

    try:
        seq.play(Pattern(ROSANNA), kit=2)
    except KeyboardInterrupt:
        # all notes off
        midi.control_change(123, 0)


if __name__ == '__main__':
    _test()
