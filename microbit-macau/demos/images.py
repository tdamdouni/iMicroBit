# comprehensive list of all built-in images:

from microbit import *


imgs = ['HEART', 'HEART_SMALL', 'HAPPY', 'SMILE', 'SAD', 'CONFUSED', 'ANGRY',
        'ASLEEP', 'SURPRISED', 'SILLY', 'FABULOUS', 'MEH', 'YES', 'NO',
        'CLOCK12', 'CLOCK11', 'CLOCK10', 'CLOCK9', 'CLOCK8', 'CLOCK7', 'CLOCK6',
        'CLOCK5', 'CLOCK4', 'CLOCK3', 'CLOCK2', 'CLOCK1', 'ARROW_N', 'ARROW_NE',
        'ARROW_E', 'ARROW_SE', 'ARROW_S', 'ARROW_SW', 'ARROW_W', 'ARROW_NW',
        'TRIANGLE', 'TRIANGLE_LEFT', 'CHESSBOARD', 'DIAMOND', 'DIAMOND_SMALL',
        'SQUARE', 'SQUARE_SMALL', 'RABBIT', 'COW', 'MUSIC_CROTCHET',
        'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'PITCHFORK', 'XMAS', 'PACMAN',
        'TARGET', 'TSHIRT', 'ROLLERSKATE', 'DUCK', 'HOUSE', 'TORTOISE',
        'BUTTERFLY', 'STICKFIGURE', 'GHOST', 'SWORD', 'GIRAFFE', 'SKULL',
        'UMBRELLA', 'SNAKE']

i = 0
display.show(getattr(Image, imgs[0]))

while True:
    sleep(100 )
    
    if button_a.get_presses() > 0:
        i = (i - 1) % len(imgs)
        display.show(getattr(Image, imgs[i]))
    if button_b.get_presses() > 0:
        i = (i + 1) % len(imgs)
        display.show(getattr(Image, imgs[i]))
