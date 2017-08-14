import music
from microbit import *
dot28 = Image("99999:""99999:""99999:""99999:""99999")
notes = ['c8:1','c#']


display.clear()

while True:
    if accelerometer.was_gesture('face up'):
        display.show(dot28)
        while button_a.is_pressed() == False:
            music.play(notes)
        sleep(1000)
        display.clear()
