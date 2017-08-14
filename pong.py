"""
Pong: A simple but fun two player game for the microbit.

Use buttons A and B to push the pixel to the other side.
The player who gets the pixel/ball over to the opposite side is the winner.
"""

from microbit import display, accelerometer, sleep, button_a, button_b
from music import play, POWER_UP


def wait_for_button():
    while not button_a.is_pressed() and not button_b.is_pressed():
        sleep(100)


def fade_display(fade=-3):
    """Loop over every pixel and reduce the brightness by the fade value."""
    for x in range(0, 5):
        for y in range(0, 5):
            current = display.get_pixel(x, y)
            faded = max(0, current + fade)
            display.set_pixel(x, y, faded)


def set_pixel(x=2, y=2):
    """Set the specified pixel to max brightness and fade everything else."""
    fade_display()
    return display.set_pixel(x, y, 9)


def play_intro(accelerometer_sensitivity=1/300):
    """Play animation of pixel moving side to side."""
    y = 2
    while not button_a.is_pressed():
        for x in [0, 1, 2, 3, 4, 3, 2, 1]:
            set_pixel(x, y)
            delta = accelerometer.get_y() * accelerometer_sensitivity
            y = max(0, min(4, int(y + delta)))
            sleep(100)


def start_countdown(count=3):
    """Play a countdown animation for the specified number of seconds."""
    for i in range(count, 0, -1):
        display.show(str(i))
        play('C:1')
        sleep(1000)
    play('A:3')
    display.clear()


def show_winner(winner):
    """Display the winner."""
    play(POWER_UP, wait=False)
    display.show(winner)
    sleep(1000)


def play_game(delay=100, accelerometer_sensitivity=1/300):
    """Enter game main event loop."""
    x, y = 2, 2   # Pixel coordinates, starting in middle of display
    winner = None
    while winner is None:
        if button_a.is_pressed():
            x = x + 1
            play('A:1')
        if button_b.is_pressed():
            x = x - 1
            play('B:1')

        if x > 4:
            winner = 'A'
        elif x < 0:
            winner = 'B'
        else:
            # No winner - continue
            set_pixel(x, y)

        # Change row based on accelerometer angle
        delta = accelerometer.get_y() * accelerometer_sensitivity
        y = max(0, min(4, int(y + delta)))

        sleep(delay)

    return winner


play_intro()
while True:
    start_countdown()
    winner = play_game()
    show_winner(winner)
    wait_for_button()
