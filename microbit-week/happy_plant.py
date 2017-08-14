from microbit import *
import math

KNOWN_RES = 1181
V_IN = 3

R_BAD = 900
R_OK = 700

BAD = (
    (9, 9, 0, 9, 9),
    (0, 9, 0, 9, 0),
    (0, 0, 0, 0, 0),
    (0, 9, 9, 9, 0),
    (9, 0, 0, 0, 9),
)

OK = (
    (0, 9, 0, 9, 0),
    (0, 9, 0, 9, 0),
    (0, 0, 0, 0, 0),
    (9, 9, 9, 9, 9),
    (0, 0, 0, 0, 0),
)

GOOD = (
    (0, 9, 0, 9, 0),
    (0, 9, 0, 9, 0),
    (0, 0, 0, 0, 0),
    (9, 0, 0, 0, 9),
    (0, 9, 9, 9, 0),

)


def to_display(matrix):
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            display.set_pixel(x, y, col)


def get_res():
    pin_val = pin0.read_analog()
    v_out = (V_IN * pin_val) / 1023
    return math.fabs(KNOWN_RES * (1 / (V_IN / v_out) - 1))


while True:
    res = get_res()
    print(res)

    if res > R_BAD:
        to_display(BAD)
    elif res > R_OK:
        to_display(OK)
    else:
        to_display(GOOD)
    print(res)
    sleep(500)
