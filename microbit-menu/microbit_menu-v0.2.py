'''
	MicrobitMenu v0.2

	Author: aztec1337
	Github: https://github.com/aztec1337/microbit-menu/

	Licensed under the GNU General Public License Version 3 (GNU GPL v3),
	available at: http://www.gnu.org/licenses/gpl-3.0.txt
'''
from microbit import *
import random
menuAmount = 1  # Start at 0
menu = 0
void = 0

while True:
    if menu == 0:
        if void == 0:
            display.scroll("DICE")
            void = 1
    elif menu == 1:
        if void == 0:
            display.scroll("LETTER")
            void = 1
    if button_a.is_pressed():
        menu += 1
        if menu > menuAmount:
            menu = 0
        void = 0
    if button_b.is_pressed():
        if menu == 0:
            display.show(str(random.randint(1, 6)))  # Random int (1 - 6)
        elif menu == 1:
            letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
            display.show(random.choice(letters))  # Choose random of alphabet
