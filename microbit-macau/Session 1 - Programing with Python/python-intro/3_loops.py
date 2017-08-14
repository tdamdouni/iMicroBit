############# ignore this bit for now #############
from microbit import *

def was_pressed():
    sleep(500)
    return button_a.was_pressed() or button_b.was_pressed()

display.show(Image.ASLEEP)

############# edit below #############

# the expression "was_pressed()" will return a bool
# telling you whether any of the buttons were pressed.
# It will also assure that half a second has passed

# write code that is waiting until one of the buttons is pressed
# and also keeps track of the number of seconds it took for this to happen
# in this variable:
time_passed = 0
    


############# edit above #############

display.scroll('It took you ' + str(time_passed) + ' seconds to wake me up.')
display.show(Image.HAPPY)
