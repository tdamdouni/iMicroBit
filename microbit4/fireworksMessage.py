# Display message and show pacman with firework option
from microbit import *

firework1 = Image("00000:00000:00000:00000:00200")
firework2 = Image("00000:00000:00000:00200:00100")
firework3 = Image("00000:00000:00200:00100:00000")
firework4 = Image("00000:00000:00900:00000:00000")
firework5 = Image("00000:07870:08580:07870:00000")
firework6 = Image("60706:01210:72127:01210:60706")
firework7 = Image("30503:00000:50005:00000:30503")
firework8 = Image("10201:00000:20002:00000:10201")
all_firework = [firework1, firework2, firework3, firework4, firework5, firework6, firework7, firework8]

while True:
    if button_a.is_pressed():
        display.clear()
        display.show(all_firework, delay=200)
        display.clear()
    elif button_b.is_pressed():
        display.clear()
        display.scroll('Hi!')
        display.show(Image.PACMAN)
        sleep(1000)
        display.clear()
    elif accelerometer.was_gesture("shake"):
        display.show(Image.CONFUSED)
        sleep(5000)
        display.clear()
    else:
        display.clear()
        display.show(Image.HAPPY)
