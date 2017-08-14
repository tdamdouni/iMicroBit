"""
Simple die simulator. Shake and then leave for 2 seconds to see the result.

Whilst shaking press either button to cheat!
"""

import microbit

# all 6 dice faces
dice_faces = [
              "     \n"
              "     \n"
              "  9  \n"
              "     \n"
              "     \n",

              "9    \n"
              "     \n"
              "     \n"
              "     \n"
              "    9\n",

              "9    \n"
              "     \n"
              "  9  \n"
              "     \n"
              "    9\n",

              "9   9\n"
              "     \n"
              "     \n"
              "     \n"
              "9   9\n",

              "9   9\n"
              "     \n"
              "  9  \n"
              "     \n"
              "9   9\n",

              "9   9\n"
              "     \n"
              "9   9\n"
              "     \n"
              "9   9\n",
             ]

# convert them to images so they can be displayed directly
dice_faces = [microbit.Image(x) for x in dice_faces]

result = 0
result_countdown = int(2000/50) # pretend we started with shaking
last_accelerometer = microbit.accelerometer.get_values()
cheating_enabled = False

# not sure if this is needed, but pretend to seed the random generator
for _ in range(last_accelerometer[0]):
    microbit.random(10)


# main loop
while True:
    microbit.sleep(50)

    # get accelerometer difference between now and last 50ms
    current_accelerometer = microbit.accelerometer.get_values()

    dx = last_accelerometer[0] - current_accelerometer[0]
    dy = last_accelerometer[1] - current_accelerometer[1]
    dz = last_accelerometer[2] - current_accelerometer[2]

    last_accelerometer = current_accelerometer

    # let's say we have shaken the board if diff >= 1000^2
    is_shaking = (dx*dx + dy*dy + dz*dz) >= 1000*1000

    # if we stopped shaking, count down to zero for the dice result
    # if we're still shaking, (re)initialise the counter
    if is_shaking:
        result_countdown = int(2000/50) # 2 seconds countdown

        # whilst shaking, check if either button is pressed. If so, enable cheating
        if microbit.button_a.is_pressed() or microbit.button_b.is_pressed():
            cheating_enabled = True

    # choose random (temporary) result if we're still counting down
    if result_countdown > 0:
        result = microbit.random(6)
        result_countdown -= 1

    # if we haven't reached countdown, display temporary result
    if result_countdown > 0:
        microbit.display.show(dice_faces[result])

        # make the display look more random by adding some dots.
        # display fewer dots as we're getting closer to the result
        for _ in range(microbit.random(int(result_countdown/5))):
            microbit.display.set_pixel(microbit.random(5),
                                       microbit.random(5),
                                       microbit.random(10))
    else:
        # we've reached the countdown, so display the result

        # show 6 if we're cheating
        if cheating_enabled:
            result = 5

        microbit.display.show(dice_faces[result])
        cheating_enabled = False
