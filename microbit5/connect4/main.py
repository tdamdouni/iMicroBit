from microbit import *
import radio

radio.config(channel=86)
radio.on()


def sb(board):
    radio.send(board)
    display.show(Image(board))


def sbp(x, y, board, new_value):
    pos = get_pos(x, y)
    board = board[:pos] + str(new_value) + board[pos+1:]
    return board


def gbp(x, y, board):
    pos = get_pos(x, y)
    value = board[pos]
    return value

def fall(x, y, board, color):
    pos = get_pos(x, y)
    sbp(x, y, board, color)
    sb(board)
    stop = False
    while not stop:
        if y >= 4 or gbp(x, y+1, board) != "0":
            stop = True
        else:
            y += 1
            board = sbp(x, y, board, color)
            board = sbp(x, y-1, board, 0)
            sb(board)
            sleep(500)
    return board
        


def get_pos(x, y):
    pos = (6*y) + x
    return pos
board = "00000:" \
        "00000:" \
        "00000:" \
        "00000:" \
        "00000:"
sb(board)


x = 4
y = 0
myTurn = True
ok = False
while True:
    if myTurn:
        if button_a.is_pressed():
            x += 1
            if x >= 5:
                x = 0
                board = sbp(4, y, board, 0)
            else:
                board = sbp(x-1, y, board, 0)
            board = sbp(x, y, board, 9)
            sb(board)
            sleep(250)
        if button_b.is_pressed():
            board = fall(x, y, board, 9)
            display.show(Image(board))
            myTurn = False
            radio.send("YT")
    else:
        data = radio.receive()
        if data:
            if data == "YT":

                myTurn = True

            else:
                board = data
                display.show(Image(data))
        
        
                
            