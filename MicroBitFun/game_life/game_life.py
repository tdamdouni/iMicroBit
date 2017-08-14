import random
from microbit import *  


ON = 9
OFF = 0
BOARD = [[OFF]*5 for i in range(5)]
ALL_INDEXES = [(i, j) for i in range(5) for j in range(5)]


def init():
    display.clear()
    num_live = random.randint(10, len(ALL_INDEXES)-10)
    live_indexes = [random.choice(ALL_INDEXES) for i in range(num_live)]
    for i, j in live_indexes:
        BOARD[i][j] = ON
    show_board()
        
def get_near(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y):
               yield i % 5, j % 5
               
def next_step():
    changed = False
    old_board = [row[:] for row in BOARD]
    for x, y in ALL_INDEXES:
        count = sum(1 for i, j in get_near(x, y) if old_board[i][j])
        value = old_board[x][y]
        #print (count, value, x, y, list(get_near(x, y)))
        if value:
            if count < 2 or count > 3:
                BOARD[x][y] = OFF
                changed = True
        else:
            if count == 3:
                BOARD[x][y] = ON
                changed = True
    if changed:
        show_board()
    return changed
    
def show_board():
    for x, y in ALL_INDEXES:
        display.set_pixel(x, y, BOARD[x][y])
    
init()
while 1:
    changed = next_step()
    if not changed:
        sleep(2000)
        if not any(i for row in BOARD for i in row):
            display.show(Image.SAD)
        else:
            display.show(Image.HAPPY)
        sleep(500)
        init()
    if button_a.is_pressed() and button_a.was_pressed():
        init()
    if button_b.is_pressed() and button_b.was_pressed():
        next_step()
    sleep(200)
