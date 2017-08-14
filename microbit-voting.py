# Micro:bit Voting Application
# Copyright Owen Maple, All Rights Reserved
from microbit import * # This imports the micro:bit packages from the micro:bit

# The variables below are set to 0 to create the variable for use in the following code
votea = 0
voteb = 0
startup = 0

# A while statement is used to continuously loop the code within it, this is required for the Micro:bit to function properly
while True:
    # The if statement below checks whether the variable startup is set to 0, if it is then it will instruct the user what to do, if not then the voting program will run
    if startup == 0:
        display.scroll("Vote A or B")
        startup = 1
        display.clear() # This clears the screen of current content
    else:
        # The if statement below activates when the A button is pressed, it is detected by a function within the micro:bit packages
        if button_a.is_pressed():
            votea = votea + 1 # Adds 1 vote to the votea variable
            display.show(str(votea)) # This converts the variable votea into a string and shows it on the micro:bit display
            sleep(500)
            display.clear()
        # The eflif statement below activates when the B button is pressed, it is is detected by a function within the micro:bit packages
        elif button_b.is_pressed():
            voteb = voteb + 1 # Adds 1 vote to the voteb variable
            display.show(str(voteb)) # This converts the variable voteb into a string and shows it on the micro:bit display
            sleep(500)
            display.clear()
        # The elif statement below activates when the device is shaken, it is detected by an accelerometer and functions within the micro:bit packages
        elif accelerometer.was_gesture("shake"):
            display.scroll("A:" + str(votea) + " B:" + str(voteb) + " ")
            display.clear()
