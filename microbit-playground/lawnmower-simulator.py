"""
Adaptation of Advanced Lawnmower Simulator
[http://www.worldofspectrum.org/infoseekid.cgi?id=0000089]

Press button A to mow the lawn. Remember that grass keeps growing!
"""

import microbit


# lawn. 0=mowed, 255=overgrown
lawn = bytearray([microbit.random(100)+100 for _ in range(5*5)])

# position of the player (x, y)
player_x, player_y = 0, 0
player_brightness = 9
player_moved = False

# main loop
while True:

    # grow the lawn, clip values at 255
    for i, v in enumerate(lawn):
        # 95 in 100 chance grass grows
        if microbit.random(100) < 95:
            lawn[i] = min(v+1, 255)

    # display lawn and the player
    for y in range(5):
        for x in range(5):
            # displaying player?
            if player_x == x and player_y == y:
                # player
                v = player_brightness
            else:
                # grass
                v = int(lawn[y*5+x]/26)

            microbit.display.set_pixel(x, y, v)

    # keep toggling player brightness between 5 and 9
    player_brightness ^= 5^9

    # move player if button is pressed (but move only by one position)
    if not player_moved:
        if microbit.button_a.is_pressed():
            player_moved = True

            # mow the grass at current square (imperfectly, i.e. not 0)
            lawn[player_y*5+player_x] = microbit.random(5)

            # move the player to the next square
            player_x += 1
            if player_x > 4:
                player_x, player_y = 0, (player_y+1) % 5
    else:
        # player moved so wait until we depress the button
        if not microbit.button_a.is_pressed():
            player_moved = False

    microbit.sleep(10)
