import microbit
import random


class GameOfLife:
    def __init__(self, size=None, data=None):
        if data:
            self.set_data(data, size or len(data))
        else:
            self.randomize(size)

    def set_data(self, data, size):
        self.pos = (0, 0)
        self.size = size
        self.data = data

    def randomize(self, size):
        if size > 30:
            raise ValueError('Size must be <30')
        self.set_data([random.getrandbits(size) for i in range(size)], size)

    def get_pixel(self, x, y):
        x %= self.size
        y %= self.size
        return self.data[y] >> (self.size - x - 1) & 1

    def set_pixel(self, x, y, value):
        x %= self.size
        y %= self.size
        bit = 1 << (self.size - x - 1)
        self.data[y] |= bit
        if not value:
            self.data[y] -= bit

    def update_row(self, y, ncs):
        for x in range(self.size):
            if ncs[x] == 3:
                self.set_pixel(x, y, 1)
            elif ncs[x] != 2:
                self.set_pixel(x, y, 0)

    def step(self):
        first_line = self.data[0]  # Save for calculating last line.
        prv, cur, nxt = None, None, [0] * self.size
        for y in range(-1, self.size + 1):
            if y == self.size:
                first_line, self.data[0] = self.data[0], first_line
            for x in range(self.size):
                if self.get_pixel(x, y):
                    px = (x - 1) % self.size
                    nx = (x + 1) % self.size
                    if prv:
                        prv[px] += 1
                        prv[x] += 1
                        prv[nx] += 1
                    if cur:
                        cur[px] += 1
                        cur[nx] += 1
                    nxt[px] += 1
                    nxt[x] += 1
                    nxt[nx] += 1
            if prv:
                self.update_row(y - 1, prv)
            prv, cur, nxt = cur, nxt, [0] * self.size
            if y == self.size:
                first_line, self.data[0] = self.data[0], first_line

    def gen_image(self):
        img_data = []
        for dy in range(5):
            for dx in range(5):
                value = self.get_pixel(self.pos[0] + dx, self.pos[1] + dy)
                img_data.append('9' if value else '0')
            img_data.append(':')
        return microbit.Image(''.join(img_data[:-1]))

    def move(self, dx, dy):
        x = (self.pos[0] + dx) % self.size
        y = (self.pos[1] + dy) % self.size
        self.pos = (x, y)

    def is_alive(self):
        return any(self.data)


SIZE = 24
CLOCK = 20
SCROLL_DELAY = 700

while __name__ == '__main__':
    game = GameOfLife(size=SIZE)
    time = 0
    scrolling = False

    while True:
        changed = False
        microbit.sleep(CLOCK)
        time += CLOCK
        if not scrolling:
            game.step()
            changed = True
            if not game.is_alive():
                break
        if microbit.button_a.was_pressed():  # Pause/resume.
            scrolling = True
            time = 0
            acc_x = max(-1, min(1, microbit.accelerometer.get_x() // 500))
            acc_y = max(-1, min(1, microbit.accelerometer.get_y() // 500))
            game.move(acc_x, acc_y)
            changed = True
        if time > SCROLL_DELAY:
            scrolling = False
        if changed:
            microbit.display.show(game.gen_image())
