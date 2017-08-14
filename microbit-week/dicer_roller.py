from microbit import *
import math

DICE_SET = (4, 6, 8, 10, 12, 20)
DEFAULT_DIE = 6
SHAKE_SPEED_THRESHOLD = 2000
SHAKE_TIME_THRESHOLD = 4 * 1000
SHAKE_EVENTS_THRESHOLD = 6


class Roller(object):
    def __init__(self):
        self.tick()
        self.current_die = DEFAULT_DIE
        self.last_roll = None
        self.last_shake_event = self.last_accel_change = self.now
        self.last_coords = accelerometer.get_values()
        self.shake_events = 0

    def tick(self):
        self.now = running_time()

    def shake_thresholds_reached(self):
        return (
            self.shake_events >= SHAKE_EVENTS_THRESHOLD and
            self.diff_since_last_shake() < SHAKE_TIME_THRESHOLD * 1000
        )

    def get_result(self, max=None):
        return random(min(self.current_die, max or self.current_die) + 1) + 1

    def select_die(self, direction=1):
        next_index = DICE_SET.index(self.current_die) + direction
        next_index = next_index if next_index < len(DICE_SET) else 0
        next_index = next_index if next_index >= 0 else len(DICE_SET) - 1
        return DICE_SET[next_index]

    def get_die(self):
        if button_a.was_pressed():
            new_die = self.select_die(-1)
        elif button_b.was_pressed():
            new_die = self.select_die()
        else:
            new_die = self.current_die
        changed = new_die != self.current_die
        self.current_die = new_die
        return self.current_die, changed

    def diff_since_last_shake(self):
        return self.now - self.last_shake_event

    def diff_since_last_acceleration(self):
        return self.now - self.last_accel_change

    def check_for_roll(self):
        time_diff = self.diff_since_last_acceleration()
        if time_diff > 100:
            self.last_accel_change = self.now
            x, y, z = accelerometer.get_values()
            last_x, last_y, last_z = self.last_coords
            speed = math.fabs(x + y + z - last_x - last_y - last_z) / time_diff * 1000
            if speed > SHAKE_SPEED_THRESHOLD:
                self.shake_events += 1
            else:
                self.shake_events = max(self.shake_events - 1, 0)

            if self.shake_thresholds_reached():
                print("Roll at {}".format(speed))
                self.shake_events = 0
                return True

            self.last_coords = x, y, z
        return False

    def roll(self):
        self.roll_animation()
        result = self.get_result()
        if len(str(result)) > 1:
            display.scroll(str(result))
        else:
            display.show(str(result))
        sleep(2000)

    def roll_animation(self):
        prev_random_num = None
        for _ in range(5):
            random_num = self.get_result(max=9)
            if prev_random_num != random_num:
                display.show(str(random_num))
                prev_random_num = random_num
                sleep(200)


def run():
    roller = Roller()

    while True:
        roller.tick()
        if not roller.check_for_roll():
          current_die, changed = roller.get_die()
          if changed:
              display.scroll(str(current_die), 80)
        else:
            roller.roll()

if __name__ == "__main__":
    run()
