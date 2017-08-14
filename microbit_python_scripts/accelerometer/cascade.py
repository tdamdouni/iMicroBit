from microbit import *
from math import ceil, floor, sin, pi

DEG_TO_RAD = 2*pi/360.0
WIDTH, HEIGHT = 5, 5


def draw_bitmap(bitmap):
    display.show(Image(':'.join(''.join(map(str, line)) for line in bitmap)))


def run():
    bitmap = [[0] * WIDTH for _ in range(HEIGHT)]
    t = 0
    a = DEG_TO_RAD * 360 / 5.0
    while True:
        ax, ay, az = accelerometer.get_values()
        ax /= 360
        ay /= 360
        az /= 360
        t += 1
        d = (t*15) * DEG_TO_RAD
        threshold = (t % 10) * 3
        for y in range(HEIGHT):
            for x in range(WIDTH):
                color = (sin((x*ax + y*ay)*a + d) + 1) * 9 / 2
                rounding = int(color * 10) % 10
                if rounding <= threshold:
                    color = ceil(color)
                else:
                    color = floor(color)
                bitmap[y][x] = int(color)

        draw_bitmap(bitmap)
        sleep(1)

run()
