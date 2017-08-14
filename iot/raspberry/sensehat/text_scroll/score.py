#python3
#author: Gabriel Rondon
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(0)
speed = 0.1
red = (255, 0, 0)
white = (0, 0, 0)

#user input
speed_input = input("Speed (eg. a fast like 0.05 or slow like 1.5): ")
speed = float(speed_input)
local = input("Home team: ")
print(local)
localPlacar = input("Score of " + local + ": ")
visitante = input("Away team: ")
visitantePlacar = input("Score of " + visitante + ": ")
message = local + str(localPlacar) + " " + visitante + str(visitantePlacar)
print(message)

#sensehat messages
sense.show_message(local, speed, text_colour=red, back_colour=white)
sense.show_letter(localPlacar)
sleep(2)
sense.show_message(visitante, speed, text_colour=red, back_colour=white)
sense.show_letter(visitantePlacar)
sleep(2)
print("Thank you for using Score. Bye!")
sense.clear()
