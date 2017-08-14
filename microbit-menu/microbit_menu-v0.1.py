'''
	MicrobitMenu v0.1

	Author: aztec1337
	Github: https://github.com/aztec1337/microbit-menu/

	Licensed under the GNU General Public License Version 3 (GNU GPL v3),
	available at: http://www.gnu.org/licenses/gpl-3.0.txt
'''
from microbit import *
import random

menu = 0

while True:
	if menu == 0:
		display.scroll("DICE")
		if button_b.is_pressed():
			display.show(random.randint(1, 6)) #Random int between 1 and 6
	elif menu == 1:
		display.scroll("LETTER")
		if button_b.is_pressed():
			letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
			display.show(random.choice(letters)) #Choose random of alphabet
	if button_a.is_pressed():
		menu ^= 1 #If 0 set 1; if 1 set 0