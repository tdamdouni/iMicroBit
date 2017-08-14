from microbit import *

# mini counter images
def _generate_counter_img(dots):
    values = ('5' * dots) + ('0' * (25 - dots))
    return ':'.join([values[i:i+5] for i in range(0, 25, 5)])

counter_imgs = [Image(_generate_counter_img(i)) for i in range(25)]

def get_counter_img(secs):
    return counter_imgs[secs % 25]


class Timer(object):
    def __init__(self):
        # time in microseconds
        self.time_elapsed = 0

    def reset(self):
        self.time_elapsed = 0

    def start_timing(self):
        self.start_time = running_time()
        return self.start_time

    def stop_timing(self):
        self.time_elapsed += running_time() - self.start_time

    def display(self):
        time = self.time_elapsed + running_time() - self.start_time
        img = get_counter_img(time // 1000)
        display.show(img)


timer = Timer()

display.show(Image.ARROW_E)

while True:
    if button_a.get_presses() > 0:
        timer.reset()
        display.show(Image.ARROW_E)

    if button_b.get_presses() > 0:
        timer.start_timing()
        while button_b.get_presses() == 0:
            timer.display()
            sleep(100)
        timer.stop_timing()
        button_a.get_presses()  # cannot reset while counting

    sleep(100)
