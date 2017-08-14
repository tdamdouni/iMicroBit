from microbit import *


try:
    with open('count.txt', 'r') as count_file:
        count_str = count_file.read()
        count = int(count_str)
except:
    count = 0

while True:
    count = count + button_b.get_presses() - button_a.get_presses()
    sleep(200)
    display.scroll(str(count))

    with open('count.txt', 'w') as count_file:
        count_str = count_file.write(str(count))
