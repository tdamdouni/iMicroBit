import microbit


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





UNKNOWN = type('_', (), {'__str__': lambda _: 'UNKNOWN'})
UNKNOWN_ANGLE = UNKNOWN()
DUTY_0PC = 0
DUTY_100PC = 1023

class Servo:
    """
    Futaba S3003 - Servo
    Control System: +Pulse Width Control 1520usec Neutral
    Required Pulse: 3-5 Volt Peak to Peak Square Wave
    Operating Voltage: 4.8-6.0 Volts
    Operating Temperature Range: -20 to +60 Degree C
    Operating Speed (4.8V): 0.23sec/60 degrees at no load
    Operating Speed (6.0V): 0.19sec/60 degrees at no load
    Stall Torque (4.8V): 44 oz/in. (3.2kg.cm)
    Stall Torque (6.0V): 56.8 oz/in. (4.1kg.cm)
    Operating Angle: 45 Deg. one side pulse traveling 400usec
    Continuous Rotation Modifiable: Yes
    Direction: Counter Clockwise/Pulse Traveling 1520-1900usec
    """
    PERIOD = 20000  # microseconds
    pin = microbit.pin0

    min_pulse_width = 500  # microseconds
    mid_pulse_width = 1520
    max_pulse_width = 3000

    min_deg = 0  # degrees
    mid_deg = 90
    max_deg = 180

    max_on_time = 1200  # milliseconds
    clockwise_speed_factor = 0.85

    def __init__(self):
        print('Initialise PWM to {} μs {:.0f} ms {:.0f} Hz'.format(
            self.PERIOD, self.PERIOD/1000, 1000000./self.PERIOD))
        self.pin.set_analog_period_microseconds(self.PERIOD)
        self.angle = UNKNOWN_ANGLE
        self.point(self.mid_deg)

    def deg_to_pulse_width(self, deg):
        return rescale(
            (self.min_deg, self.max_deg),
            (self.max_pulse_width, self.min_pulse_width),
            deg
        )

    def pulse_width_to_duty_cycle_value(self, pulse_width):
        return rescale(
            (0, self.PERIOD),
            (DUTY_0PC, DUTY_100PC),
            pulse_width
        )

    def deg_to_duty_cycle_value(self, deg):
        pulse_width = self.deg_to_pulse_width(deg)
        assert self.min_pulse_width <= pulse_width <= self.max_pulse_width
        print('\tpulse width {:.0f} μs'.format(pulse_width))

        duty_cycle_value = self.pulse_width_to_duty_cycle_value(pulse_width)
        percent = rescale((0, DUTY_100PC), (0, 100), duty_cycle_value)
        print('\tduty cycle {:.0f}/{} ({:.1f}%)'.format(
            duty_cycle_value, DUTY_100PC, percent))
        return duty_cycle_value

    def calc_on_time(self, deg):
        """
        Operating Speed (4.8V): 0.23sec/60 degrees at no load
        ms_per_deg = 230 / 60.
        """
        # from observations:
        ms_per_deg = 600 / 90.
        if self.angle is UNKNOWN_ANGLE:
            return self.max_on_time / 2.
        is_clockwise = self.angle < deg
        travel = abs(deg - self.angle)
        on_time = travel * ms_per_deg

        if is_clockwise:
            on_time *= self.clockwise_speed_factor
        assert on_time <= self.max_on_time
        return on_time

    def wait_and_display_pwm(self, duty_cycle_value, on_time):
        start = microbit.running_time()
        width = round(on_time / 15)
        hits = range(0, width, round(DUTY_100PC / duty_cycle_value))
        points = [('#' if i in hits else '.') for i in range(width)]
        while True:
            microbit.sleep(1)
            duration = microbit.running_time() - start
            progress_left = 1 - (duration / on_time)
            points_left = int((width * progress_left)) + 1

            while points and len(points) > points_left:
                point = points.pop(0)
                print(point, end='', flush=True)

            if duration >= on_time:
                break
        print()

    def pulse_burst(self, duty_cycle_value, on_time):
        try:
            microbit.pin0.write_analog(duty_cycle_value)
            self.wait_and_display_pwm(duty_cycle_value, on_time)
        finally:
            # ensure we don't leave the pwm on
            microbit.pin0.write_analog(0)


    def point(self, deg):
        print('point {}° to {}°'.format(self.angle, deg))
        duty_cycle_value = self.deg_to_duty_cycle_value(deg)
        on_time = self.calc_on_time(deg)
        print('\ton for {:.0f} ms'.format(on_time))
        self.angle = deg
        self.pulse_burst(duty_cycle_value, on_time)


pause_time = 5
def demo():
    servo = Servo()
    for deg in 0, 180, 90, 180, 0:
        servo.point(deg)
        microbit.sleep(pause_time)


if __name__ == '__main__':
    demo()
