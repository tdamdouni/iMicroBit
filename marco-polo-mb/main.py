import microbit
import music
import radio


def siren(steps=16, up_only=False):
    for freq in range(880, 1760, steps):
        music.pitch(freq, 6)
    if up_only: return
    for freq in range(1760, 880, -steps):
        music.pitch(freq, 6)


class Debouncer:
    def __init__(self, cooldown_ms):
        self.cooldown = cooldown_ms
        self.last_bounced = -cooldown_ms

    def debounce(self):
        return (microbit.running_time() - self.last_bounced) < self.cooldown

    def bounce(self):
        self.last_bounced = microbit.running_time()

    def attempt(self):
        if self.debounce():
            return False
        else:
            self.bounce()
            return True


class PingPonger:
    def __init__(self,
                 pong_limit=3,
                 cooldown=500,
                 pong_function=siren):
        self.pong_limit = pong_limit
        self.pong_function = pong_function
        self.debouncer = Debouncer(cooldown_ms=cooldown)
        self.recharge()

    def recharge(self):
        self.pongs = [1] * self.pong_limit

    def ping(self):
        """
        Sends a ping, which any devices with pongs left will respond to.
        """
        radio.send_bytes(b'ping')

    def pong_on_ping(self):
        msg = radio.receive_bytes()
        if msg is None: return
        if msg == b'ping':
            self.pong()
        else:
            raise ValueError(msg)

    def pong(self):
        """
        If any pongs remain, spend one.
        """
        if self.debouncer.attempt() and self.pongs:
            self.pongs.pop()  # Spend one
            self.pong_function()
        #microbit.display.scroll("q")

def list_map_to_img(lm):
    return microbit.Image(':'.join(lm))

digits = list(map(list_map_to_img, [
    [
        '09900',
        '90090',
        '90090',
        '90090',
        '09900',
    ],
    [
        '00900',
        '09900',
        '00900',
        '00900',
        '09990',
    ],
    [
        '09900',
        '90090',
        '00900',
        '09000',
        '99990',
    ],
    [
        '09900',
        '90090',
        '00900',
        '90090',
        '09900',
    ],
    [
        '00090',
        '00990',
        '09090',
        '99999',
        '00090',
    ],
    [
        '99990',
        '90000',
        '09900',
        '00090',
        '99900',
    ],
]))

radio.on()
me_pp = PingPonger(
    pong_limit=5,
    cooldown=2000,
    pong_function=lambda:siren(steps=32, up_only=True))
me_pp.pong_function()

while True:
    me_pp.pong_on_ping()
    if microbit.button_a.was_pressed():
        #microbit.display.scroll("A")
        me_pp.ping()
    if microbit.button_b.was_pressed():
        #microbit.display.scroll("B")
        me_pp.recharge()
    microbit.display.show(digits[len(me_pp.pongs)] * (0.5 if (me_pp.debouncer.debounce()) else 1))
