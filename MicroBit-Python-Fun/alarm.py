from microbit import *


class Alarm:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.is_set = False
        self.alarm_raised = False

    def set(self):
        display.show(Image.ASLEEP)
        # this is to allow time to let the microbit be settle after you might have moved it when pressing button
        sleep(3000)

        self.x = accelerometer.get_x()
        self.y = accelerometer.get_y()
        self.z = accelerometer.get_z()
        self.is_set = True
        display.scroll("Alarm set")
        display.show(Image.YES)

    def unset(self):
        self.is_set = False
        self.alarm_raised = False
        display.show(Image.HAPPY)

    def has_been_moved(self):
        return not (accelerometer.get_x() - 50 < self.x < accelerometer.get_x() + 50 \
            or accelerometer.get_y() - 50 < self.y < accelerometer.get_y() + 50 \
            or accelerometer.get_z() - 50 < self.z < accelerometer.get_z() + 50)


def run():
    alarm = Alarm()

    while True:
        if alarm.is_set:
            if button_b.is_pressed():
                alarm.unset()
            if not alarm.alarm_raised:
                if alarm.has_been_moved():
                    alarm.alarm_raised = True
                else:
                    sleep(500)
            else:
                display.show(Image.ANGRY)
                pin0.write_digital(1)
                sleep(100)
                display.clear()
                pin0.write_digital(0)
                sleep(100)
        else:
            if button_a.is_pressed():
                alarm.set()

if __name__ == "__main__":
    run()
