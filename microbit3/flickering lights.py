from microbit import *

frame1 = Image("00000:00000:00000:99999:99999")
frame2 = Image("99999:99999:00000:00000:00000")

frames = [frame1,frame2]

while True:
    display.show(frames,delay = 1)
