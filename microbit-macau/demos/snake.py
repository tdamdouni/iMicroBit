from microbit import *
import random

# number of time intensity of apple changes per movement of snake
_FRAME_COUNT = 14

# Directions
N = (-1, 0)
W = (0, -1)
S = (1, 0)
E = (0, 1)

def turn_left(direction):
    if direction == N:
        return W
    if direction == W:
        return S
    if direction == S:
        return E
    return N

def turn_right(direction):
    if direction == N:
        return E
    if direction == E:
        return S
    if direction == S:
        return W
    return N

# Get next position given initial position and direction.
def get_next(pos, direction):
    return ((pos[0] + direction[0])%5, (pos[1] + direction[1])%5)


class Snake(object):
    # Snake object stores current position(s), boolean (whether it's growing),
    # and current directions.
    def __init__(self):
        self.parts = [(2,2)]
        self.direction = E
        self.grows = False

    # head of the snake
    def head(self):
        return self.parts[0]

    # Change position of the snake according to direction.
    # True if snake doesn't collide with itself, False otherwise (game lost).
    def move(self):
        new = get_next(self.head(), self.direction)
        if self.grows:
            self.parts.insert(0, new)
            self.grows = False
        else:
            self.parts.pop()
            self.parts.insert(0, new)

        if new in self.parts[1:]:
            return False
        return True

    # length of the snake
    def __len__(self):
        return len(self.parts)


class Board(object):
    def __init__(self, snake):
        self.snake = snake
        self.tiles = [[0] * 5] + [[0] * 5] + [[0] * 5] + [[0] * 5] + [[0] * 5]
        self.apples = []
        # generate two apples
        self.add_random_apple()
        self.add_random_apple()

        # count number of frames; apple-pixels change more frequently than the
        # snake moves
        self.frame_count = 0
        # apples are distinguishable by (rapidly) changing intensity
        self.apple_intensity = 0

    # set a position (tuple) to a
    def set(self, pos, intensity):
        self.tiles[pos[0]][pos[1]] = intensity

    # Choose a random position that is not occupied.
    # Choosing out of a list of free positions is not feasable due to
    # memory limitations.
    def add_random_apple(self):
        free = 25 - len(self.snake.parts) - len(self.apples)
        if free == 0:
            return  # can't add another apple

        i = -1
        for k in range(random.randint(1, free)):
            i += 1
            while (i//5, i%5) in self.snake.parts or (i//5, i%5) in self.apples:
                i += 1
        self.apples.append((i // 5, i % 5))

    def draw_snake(self):
        slen = len(self.snake)
        if slen < 9:
            for pos, intensity in zip(self.snake.parts, range(9, 1, -1)):
                self.set(pos, intensity)
        else:
            tail_part_size = slen // 8
            head_size = slen - tail_part_size * 7
            # set the 8 parts of the tail to intensities 2,..,8
            for i in range(8, 1, -1):
                beg = head_size + (8-i) * tail_part_size
                part = self.snake.parts[beg:beg + tail_part_size]
                for pos in part:
                    self.set(pos, i)
            # set the front part of the snake to highest intensity 9
            for pos in self.snake.parts[0:head_size]:
                self.set(pos, 9)

    def draw(self):
        for xy in range(25):
            display.set_pixel(xy%5, xy//5, self.tiles[xy//5][xy%5])

    def step(self):
        if self.frame_count == 0:
            # clear tiles
            for line in self.tiles:
                for j in range(len(line)):
                    line[j] = 0

            # move snake
            if self.snake.move() == False:
                return 'l'
            if len(self.snake) == 30:
                return 'w'

            if self.snake.head() in self.apples:
                self.apples.remove(self.snake.head())
                self.add_random_apple()
                self.snake.grows = True

            self.draw_snake()

        # draw apple tiles
        self.apple_intensity += 1
        self.apple_intensity %= 8
        for apple in self.apples:
            self.set(apple, 2 + self.apple_intensity)

        self.draw()

        self.frame_count += 1
        self.frame_count %= _FRAME_COUNT

        return 'c'

while True:
    snake = Snake()
    board = Board(snake)

    state = board.step()

    while  state == 'c':
        if button_a.get_presses() > 0:
            snake.direction = turn_left(snake.direction)
        elif button_b.get_presses() > 0:
            snake.direction = turn_right(snake.direction)
        sleep(50)

        state = board.step()

    if state == 'w':
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

    while button_a.was_pressed() or button_b.was_pressed():
        sleep(200)
