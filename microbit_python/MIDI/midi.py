from microbit import *

class MIDI():
    NOTE_ON  = 0x90
    NOTE_OFF = 0x80
    CHAN_MSG = 0xB0
    CHAN_BANK = 0x00
    CHAN_VOLUME = 0x07
    CHAN_PROGRAM = 0xC0

    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

    @staticmethod
    def send(b0, b1, b2=None):
        if b2 is None: m = bytes([b0,b1])
        else: m = bytes([b0,b1,b2])
        uart.write(m)

    def __init__(self, channel=0, velocity=0x7F):
        self.channel = channel
        self.velocity = velocity
        
    def set_instrument(self, instrument):
        instrument -= 1
        if instrument<0 or instrument>0x7F: return
        self.send(self.CHAN_PROGRAM|self.channel, instrument)

    def note_on(self, note, velocity=None):
        if note<0 or note>0x7F:return
        if velocity is None: velocity=self.velocity
        if velocity<0 or velocity>0x7F: velocity=0x7F
        self.send(self.NOTE_ON|self.channel, note, velocity)

    def note_off(self, note, velocity=0x7F):
        if note<0 or note>0x7F:return
        if velocity is None: velocity=self.velocity
        if velocity<0 or velocity>0x7F: velocity=0x7F
        self.send(self.NOTE_OFF|self.channel, note, velocity)

midi = MIDI()

def slide():
    while True:
        for n in range(20, 90):
            midi.note_on(n)
            sleep(10)
            midi.note_off(n)
            sleep(10)

def acc():
    min_n = 20 # 0
    max_n = 90 # 127
    prev_n = None
    while True:
        x = accelerometer.get_x()
        x = min(x, 1000)
        x = max(x, -1000)
        x += 1000
        n = min_n + x / (2000/(max_n-min_n))
        n = int(n)
        
        if prev_n is None or prev_n != n:
            if prev_n is not None:
                midi.note_off(prev_n)
             
            midi.note_on(n)
            prev_n = n
        
acc()

