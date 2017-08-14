############# ignore this bit for now #############
from microbit import *


############# edit below #############

# your variable is going to be shown on the microbit
my_var = 42

############# edit above #############

while True:
    display.scroll(str(my_var))
    sleep(500)