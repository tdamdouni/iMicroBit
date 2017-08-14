try:
    from microbit import running_time, sleep
except ImportError:
    # for regular Python
    from time import sleep as tsleep, time

    def running_time():
        return time() * 1000
    def sleep(t):
        return tsleep(t / 1000)


# Start OF SEQUENCER CODE
# -----------------------------------------------------------------------------
#
# Copy everything below here until the END OF SEQUENCER CODE line
# to the *start* of your micro:bit MicroPython script
# in which you want to use the drum sequencer.

class Pattern:
    velocities = {
        "-": None, # continue note
        ".": 0,    # off
        "+": 10,   # ghost
        "s": 60,   # soft
        "m": 100,  # medium
        "x": 120,  # hard
    }

    def __init__(self, src):
        self.step = 0
        self.instruments = []
        self._active_notes = {}
        pattern = (line.strip() for line in src.split('\n'))
        pattern = (line for line in pattern
                   if line and not line.startswith('#'))

        for line in pattern:
            parts = line.split(" ", 2)

            if len(parts) == 3:
                note, hits, description = parts
            elif len(parts) == 2:
                note, hits = parts
                description = None
            else:
                continue

            note = int(note)
            self.instruments.append((note, hits))

        self.steps = max(len(hits) for _, hits in self.instruments)

    def playstep(self, midiout, channel=10):
        for note, hits in self.instruments:
            velocity = self.velocities.get(hits[self.step])

            if velocity is not None:
                if self._active_notes.get(note):
                    # velocity==0 <=> note off
                    midiout.note_on(note, 0, ch=channel)
                    self._active_notes[note] = 0
                if velocity > 0:
                    midiout.note_on(note, max(1, velocity), ch=channel)
                    self._active_notes[note] = velocity

        self.step = (self.step + 1) % self.steps


class Sequencer:
    def __init__(self, midiout, bpm=120, channel=10, volume=127):
        self.midiout = midiout
        self.mpt = 15000. / max(20, min(bpm, 400))  # millisec per tick (1/16)
        self.channel = channel
        self.volume = volume

    def play(self, pattern, kit=None):
        # channel volume
        self.midiout.control_change(10, self.volume, ch=self.channel)
        self.activate_drumkit(kit)
        # give MIDI instrument some time to load drumkit
        sleep(300)

        try:
            while True:
                last_tick = running_time()
                pattern.playstep(self.midiout, self.channel)
                timetowait = max(0, self.mpt - (running_time() - last_tick))
                if timetowait > 0:
                    sleep(timetowait)
        finally:
            # all sound off
            self.midiout.control_change(120, 0)

    def activate_drumkit(self, kit):
        if isinstance(kit, (list, tuple)):
            msb, lsb, pc = kit
        else:
            msb = lsb = None

        if msb is not None:
            # bank select msb
            self.midiout.control_change(0, msb, ch=self.channel)

        if lsb is not None:
            # bank select lsb
            self.midiout.control_change(32, lsb, ch=self.channel)

        if kit is not None:
            self.midiout.program_change(kit, ch=self.channel)

# END OF SEQUENCER CODE
# -----------------------------------------------------------------------------
