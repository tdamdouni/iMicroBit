# connect4x4  02/03/2016  D.J.Whale
#
# A 4x4 grid of connect 4 with full gameplay

from microbit import *

# winning masks for win signatures, 10 in all for a 4x4 board
# can be applied to any player board
# col,depth        bits left to right MSB to LSB
# 00 10 20 30      15 14 13 12
# 01 11 21 31      11 10 09 08
# 02 12 22 32      07 06 05 04
# 03 13 23 33      03 02 01 00

win = [
#horizontal wins (4)
# 15,14,13,12 = 1111 0000 0000 0000
0xF000,
# 11,10,09,08 = 0000 1111 0000 0000
0x0F00,
# 07,06,05,04 = 0000 0000 1111 0000
0x00F0,
# 03,02,01,00 = 0000 0000 0000 1111
0x000F,
#vertical wins (4)
# 15,11,07,03 = 1000 1000 1000 1000
0x8888,
# 14,10,06,02 = 0100 0100 0100 0100
0x4444,
# 13,09,05,01 = 0010 0010 0010 0010
0x2222,
# 12,08,04,00 = 0001 0001 0001 0001
0x1111,
#diagonal wins (2)
# 15,10,05,00 = 1000 0100 0010 0001
0x8421,
# 12,09,06,03 = 0001 0010 0100 1000
0x1248
]

# a board for each player
# 16 bit binary encoded raster for player 1[0] and player 2[1]

boards = None
def clear_board():
    global boards
    boards = [0x0000, 0x0000]

def get_brightness(player):
    if player == 1:
        return 9
    else:
        return 4
        
def splash_screen():
    """Show a splash screen until any button is pressed"""
    while True:
        display.show("C4", 500)
        if button_a.was_pressed() or button_b.was_pressed():
            break
    display.clear()
    #button_a.reset_presses()
    #button_b.reset_presses()
    
def move(player, col):
    """Move a piece along the top for this player"""
    # starts off at col
    # button A moves left, until leftmost position
    # button B moves right, until rightmost position
    # button A+B requests a drop
    # draws a dot at top row
    # intensity is bright for player 1, dim for player 2
    # returns column selected (0..3)

    #button_a.reset_presses()
    #button_b.reset_presses()
    brightness = get_brightness(player)
    display.set_pixel(col, 0, brightness)
        
    while accelerometer.get_y() < 800:
        if button_a.was_pressed():
            if col > 0:
                display.set_pixel(col, 0, 0)
                col -= 1
                display.set_pixel(col, 0, brightness)
                
        elif button_b.was_pressed():
            if col < 3:
                display.set_pixel(col, 0, 0)
                col += 1
                display.set_pixel(col, 0, brightness)
                
    display.set_pixel(col, 0, 0)
    return col
    
def get_depth(col):
    """Work out how far to drop a piece down this column until it stops"""
    # scans down the column finding the first full piece for any player
    # returns 0 if the column is full
    # returns 1 if there is 1 space left, 2, 3.

    # 'or' together both boards to get occupancy signature
    occupancy = boards[0] | boards[1]

    # highest 3-(set bit number in nibble) (3210) is depth of that col
    # build a mask for the col by shifting a 1 into the nibble position of top row
    mask = 0x8000 >> col
    
    # count how many rotate by 4's (max 4) before the mask finds a non zero
    for i in range(4): # 0 to 3
        if occupancy & mask != 0:
            return i # found a set bit at this depth
        mask >>= 4 # move to next row
        
    return 4 # the column is empty
    
def drop(player, col, depth):
    """Animate dropping a piece down this column until it reaches depth"""
    brightness = get_brightness(player)

    # animates dropping a piece for a player
    #   draw the player dot in the correct intensity
    #   animate from top down to depth (0 is top, 3 is bottom)
        
    for i in range(depth+1):
        display.set_pixel(col, i+1, brightness)
        sleep(750)
        display.set_pixel(col, i+1, 0)
    display.set_pixel(col, i+1, brightness)
    
    
def set(player, col, depth):
    """Remember a player token at this column and row"""
    # must set appropriate bit in board for that player at end
    #   col is index into nibble (how many shifts of 4bits)
    #   row is bit number in nibble (how many shifts)
    mask = 0x8000 >> ((depth*4) + col)
    boards[player-1] |= mask
    brightness = get_brightness(player)
    display.set_pixel(col, depth+1, brightness)
   
def get_winner():
    """Work out if there is a winner"""
    for pi in range(2):
        p = boards[pi]
        for sig in win:
            if p & sig == sig:
                return pi+1 # This player 1 or 2 is a winner

    # no winner
    # are all positions occupied?
    occupancy = boards[0] | boards[1]
    if occupancy == 0xFFFF:
        return -1 # stalemate
        
    return 0 # no player is a winner yet
    
def winner(player):
    """Show winner or stalemate animation"""
    # show a flashing player number then solid at end
    # note player -1 means stale mate
    # at end, wait for any button press to exit

    if player == -1:
        ch = "X" # stale mate
    else:
        ch = str(player)
        
    for i in range(4):
        display.show(ch)
        sleep(500)
        display.clear()
        sleep(500)
    display.show(ch)
    sleep(2000)
        
def run(): 
    # run forever
    while True:
        game_over = False
        player = 1
        clear_board()
        
        # show splash screen and wait for start
        splash_screen()

        # main game loop
        while not game_over:
            # get a valid move
            col = 0
            while True:
                col = move(player, col)
                depth = get_depth(col)
                if depth > 0:
                    break

            # action the move
            drop(player, col, depth-1)
            set(player, col, depth-1)
            
            # work out if the game is over
            win = get_winner()
            if win == 0:
                # swap to other player
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                # winner or stalemate
                winner(win) 
                game_over = True
 
run()

# END

