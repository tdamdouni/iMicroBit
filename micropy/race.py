import microbit
import random


# Delay in microseconds between cycles.
CLOCK = 25


class BaseHandler:
    def __init__(self):
        self.time = 0

    def tick(self, time_passed):
        self.time += time_passed


class Init(BaseHandler):

    def run(self, button_a=False, button_b=False):
        if button_a:
            return Game(), ''
        if self.time % 1000 < 500:
            return self, microbit.Image.ARROW_W
        return self, microbit.Image.HAPPY


class Game(BaseHandler):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.field = [[0] * 5] * 5
        self.pos = 2
        self.delay = 500
        self.time = 0

    def crashed(self):
        return self.field[4][self.pos] != 0

    def forward(self):
        self.time = self.time % self.delay
        self.row += 1
        new_row = [0] * 5
        if self.row % 2:
            new_row[random.randint(0, 4)] = 5
        self.field = [new_row] + self.field[:4]
        self.delay -= self.delay // 50

    def run(self, button_a=False, button_b=False):
        if self.crashed():
            return EndGame(self.row), None

        if button_a:
            self.pos = max(0, self.pos - 1)
        if button_b:
            self.pos = min(4, self.pos + 1)

        if self.time >= self.delay:
            self.forward()

        frame_buffer = [[x for x in row] for row in self.field]
        frame_buffer[4][self.pos] = 9
        screen = microbit.Image(':'.join(''.join(map(str, row))
                                         for row in frame_buffer))
        return self, screen


class EndGame(BaseHandler):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.showing_score = False

    def run(self, button_a=False, button_b=False):
        if self.time > 1000:
            if button_a:
                return Game(), None
            if not self.showing_score:
                self.showing_score = True
                return self, 'score {}'.format(self.score)
        return self, None


if __name__ == '__main__':
    handler = Init()
    while True:
        microbit.sleep(CLOCK)
        handler.tick(CLOCK)
        handler, output = handler.run(
            button_a=microbit.button_a.was_pressed(),
            button_b=microbit.button_b.was_pressed(),
        )
        if isinstance(output, microbit.Image):
            microbit.display.show(output)
        elif isinstance(output, str):
            microbit.display.scroll(output, wait=False, loop=True)
