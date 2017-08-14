from microbit import *

asleep = False

while True:
    gesture = accelerometer.current_gesture()

    if not asleep:
        if gesture == "face up" and not asleep:
            display.show(Image.HAPPY)
        elif gesture == "face down" and not asleep:
            asleep = True
            display.clear()
        else:
            display.show(Image.ANGRY)
    elif accelerometer.was_gesture("shake"):
        asleep = False
