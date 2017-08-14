'''
	MicrobitMenu v0.25

	Author: aztec1337
	Github: https://github.com/aztec1337/microbit-menu/

	Licensed under the GNU General Public License Version 3 (GNU GPL v3),
	available at: http://www.gnu.org/licenses/gpl-3.0.txt
'''
from microbit import *
import random
menuAmount = 2  # Count of menus (starting at 0)
menu = 0  # Default menu to start on
void = 0  # If text scrolled already, don't scroll again until button pressed

while True:
    if menu == 0:
        if void == 0:
            diceImage = Image("90009:00000:00900:00000:90009")  # Dice image
            display.show(diceImage)
            sleep(250)
            void = 1
    elif menu == 1:
        if void == 0:
            letterImage = Image("90000:90000:90000:90000:99990")  # Letter 'L'
	
            display.show(letterImage)
            sleep(250)
            void = 1
    elif menu == 2:
        if void == 0:
            colourImage = Image("09990:90000:90000:90000:09990")  # Letter 'C'
            display.show(colourImage)
            sleep(250)
            void = 1
    if button_a.is_pressed():  # If menu swap button is pressed
        menu += 1
        if menu > menuAmount:
            menu = 0
        void = 0
    if button_b.is_pressed():  # If function button is pressed
        if menu == 0:
            display.show(str(random.randint(1, 6)))  # Random int (1 - 6)
        elif menu == 1:
            letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            display.show(random.choice(letters))  # Choose random of alphabet
        elif menu == 2:
            colours = ["RED", "BLUE", "GREEN", "YELLOW", "PINK", "BROWN", "WHITE", "BLACK", "PURPLE"]
            display.scroll(random.choice(colours), delay = 100)
