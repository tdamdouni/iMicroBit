# Count the micro:bit's uptime dans display it under binary format
# Press A to switch between binary and decimal display
# Press B to add 1 to the counter
from microbit import *


BINARY = True
DECIMAL = False


def decimal_to_binary_img(n):
    """
    Take a number `n` and convert it into a "micro:bit ready" binary representation.
    """
    # Convert the time from base 10 to base 2 (binary) on 25 positions
    binary_n = '{0:025b}'.format(n)

    # Revert the string to start displaying in the upper left corner
    reverted_binary_n = ''.join(reversed(binary_n))

    # Convert 1 to 9 (led's the brightest luminosity)
    reverted_binary_n = reverted_binary_n.replace('1', '9')

    # Build the image
    return Image(':'.join([reverted_binary_n[i:i+5] for i in range(0, len(reverted_binary_n), 5)]))


display_format = BINARY
while True:
    button_pressed = False
    seconds = running_time() // 1000

    if button_b.was_pressed():
        button_pressed = True
        presses = button_b.get_presses()
        seconds += button_b.get_presses()
        display.scroll('+%s' % presses)

    if button_a.was_pressed():
        button_pressed = True
        display_format = not display_format

    if display_format == BINARY:
        display.show(decimal_to_binary_img(seconds))
    elif display_format == DECIMAL:
        display.scroll(str(seconds))

    if button_pressed:
        # Directly retart the loop so the change appears faster
        continue
    else:
        # Wait for a second
        sleep(1000)
