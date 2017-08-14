from microbit import running_time, display, Image

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)
