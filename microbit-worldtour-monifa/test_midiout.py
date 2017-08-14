from microbit import uart

# global constants
NOTE_OFF = 0x80
NOTE_ON = 0x90
CONTROLLER_CHANGE = 0xB0
PROGRAM_CHANGE = 0xC0

class MidiOut:
    def __init__(self, device=None, channel=1):
        if device is None:
            self.device = uart
            self.device.init(baudrate=31250)
        elif not hasattr(device, 'write'):
            raise TypeError("device instance must have a 'write' method.")
        else:
            self.device = device

        if channel < 1 or channel > 16:
            raise ValueError('channel must be an integer between 1..16.')
        self.channel = channel
    def send(self, msg):
        return self.device.write(bytes(msg))
    def channel_message(self, command, *data, ch=None):
        command = (command & 0xf0) | ((ch if ch else self.channel) - 1 & 0xf)
        msg = [command] + [value & 0x7f for value in data]
        self.send(msg)
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


# -----------------------------------------------------------------------------
# Main script

from microbit import button_a, display, sleep


while True:
    if button_a.is_pressed():
        display.set_pixel(0, 0, 0)
        break

    display.set_pixel(0, 0, 5)
    sleep(100)
    display.set_pixel(0, 0, 0)
    sleep(100)

# Initialize UART for MIDI
midi = MidiOut()

while True:
    # send NOTE ON for middle C (60) at velocity 100
    midi.note_on(60, 100)
    display.set_pixel(0, 0, 5)
    sleep(500)
    display.set_pixel(0, 0, 0)
    # send NOTE OFF
    midi.note_off(60)
    sleep(500)
