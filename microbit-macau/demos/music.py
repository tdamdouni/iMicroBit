import music
from microbit import *

pieces = ['DADADADUM', 'ENTERTAINER', 'PRELUDE', 'ODE', 'NYAN', 'RINGTONE',
         'FUNK', 'BLUES', 'BIRTHDAY', 'WEDDING', 'FUNERAL', 'PUNCHLINE',
         'PYTHON', 'BADDY', 'CHASE', 'BA_DING', 'WAWAWAWAA', 'JUMP_UP',
         'JUMP_DOWN', 'POWER_UP', 'POWER_DOWN']

def play(i):
    music.play(getattr(music, pieces[i]))
    display.scroll(pieces[i])

i = 0
display.show(Image.MUSIC_QUAVERS)

while button_b.get_presses() + button_a.get_presses() == 0:
    sleep(100)

play(0)


while True:
    sleep(100)

    if button_a.get_presses() > 0:
        i = (i - 1) % len(pieces)
        play(i)

    elif button_b.get_presses() > 0:
        i = (i + 1) % len(pieces)
        play(i)
