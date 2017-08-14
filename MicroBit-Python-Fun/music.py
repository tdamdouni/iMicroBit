from microbit import *
import music


TOLERANCE = 3000


def get_accelerometer_total():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    return x + y + z


def wait_for_shake():
    shaken = False
    last = get_accelerometer_total()
    while not shaken:
        this = get_accelerometer_total()
        diff = last - this
        if diff < 0:
            diff = diff * -1
        if diff > TOLERANCE:
            shaken = True
        last = this
        sleep(50)


twinkle_twinkle = ['c4:4', 'c', 'g', 'g', 'a', 'a', 'g:8',
                    'f:4', 'f', 'e', 'e', 'd', 'd', 'c:8',
                    'g:4', 'g', 'f', 'f', 'e', 'e', 'd:8',
                    'g:4', 'g', 'f', 'f', 'e', 'e', 'd:8',
                    'c:4', 'c', 'g', 'g', 'a', 'a', 'g:8',
                    'f:4', 'f', 'e', 'e', 'd', 'd', 'c:8']

list_of_songs = [twinkle_twinkle, music.FUNERAL, music.DADADADUM, music.BIRTHDAY, music.ENTERTAINER, music.ODE,
music.PRELUDE, music.BLUES, music.PYTHON, music.NYAN]

while True:
    wait_for_shake()
    music.stop()
    music.play(list_of_songs[random(len(list_of_songs))], wait=False)