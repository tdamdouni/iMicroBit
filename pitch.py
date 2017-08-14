from microbit import display, accelerometer, sleep, button_a, button_b
from music import pitch, stop as stop_music


def updown():
    for p in range(10, 1000, 10):
        pitch(p, wait=False)
        sleep(10)
    for p in range(1000, 10, -10):
        pitch(p, wait=False)
        sleep(10)


def accel():
    while not button_a.is_pressed():
        p = abs(accelerometer.get_z())
        pitch(p, wait=False)
        sleep(10)


while True:
    stop_music()
    display.show('?')
    if button_a.is_pressed():
        updown()
    if button_b.is_pressed():
        accel()
    sleep(10)
