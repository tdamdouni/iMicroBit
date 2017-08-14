import microbit

DUTY_0PC = 0
DUTY_100PC = 1023

def rescale(src_scale, dest_scale, x):
    """Map one number scale to another

    For example, to convert a score of 4 stars out of 5 into a percentage:
    >>> rescale((0, 5), (0, 100), 4)
    80.0

    Great for mapping different input values into LED pixel brightnesses!
    """
    src_start, src_end = src_scale
    # what proportion along src_scale x is:
    proportion = 1.0 * (x - src_start) / (src_end - src_start)

    dest_start, dest_end = dest_scale
    # apply our proportion to the dest_scale
    return proportion * (dest_end - dest_start) + dest_start


PERIOD = 5000  # microseconds

def half_duty(pulse_width, on, off):
    microbit.pin0.set_analog_period_microseconds(2 * pulse_width)
    print(pulse_width, 2 * pulse_width, end='...')
    try:
        microbit.pin0.write_analog(int(511))
        microbit.sleep(on)
    finally:
        print('#', end='')
        microbit.pin0.write_analog(0)
        print('')
    microbit.sleep(off)

def pulse_burst(pulse_width, on, off):
    microbit.pin0.set_analog_period_microseconds(PERIOD)
    pulse_value_f = rescale((0, PERIOD), (DUTY_0PC, DUTY_100PC), pulse_width)
    percent = rescale((0, PERIOD), (0, 100), pulse_value_f)
    pulse_value = round(pulse_value_f)
    print(
        "{} {} {:2.0f}%, {}".format(pulse_width, pulse_value, percent, on),
        end=' ... ',
        flush=True
    )

    try:
        microbit.pin0.write_analog(pulse_value)
        microbit.sleep(on)
    finally:
        print('#', end='')
        microbit.pin0.write_analog(0)
        print('')
    microbit.sleep(off)

on = 50
off = 0
pause = 1000
mn = 500
mx = 3000
md = 1500
step = 20
use_pulse = True
# use 600
top = 850  # 1200
bot = 700  # 900
mn_factor = 0.85
md_factor = 1.5


def range_up_then_down(mn=mn, mx=mx, step=step):
    yield from range(mn, mx, step)
    print()
    yield from range(mx, mn, -step)
    print()

def clock():
    while 1:
        for i in range_up_then_down():
            func = pulse_burst if use_pulse else half_duty
            func(i, on, off)
        print()

def clock():
    while 1:
        for o in range_up_then_down(bot, top, 100):
            print(' ' * 50, o)
            for n in mn, md, mx, md:
                od = o
                if n == mn:
                    od = round(o * mn_factor)
                if n == md:
                    od = round(o * md_factor)
                pulse_burst(n, od, off)
                print()
                microbit.sleep(pause)



if __name__ == '__main__':
    clock()
