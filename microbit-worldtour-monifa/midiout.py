# -----------------------------------------------------------------------------
# START OF MIDI LIBRARY CODE
#
# Copy everything below here until the END OF MIDI LIBRARY CODE line
# to the *start* of your micro:bit MicroPython script
# in which you want to use MIDI output.

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

    def send(self, msg):
        return self.device.send_message(bytes(msg))

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
