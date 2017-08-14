from microbit import *
#from microbit import speech
#from microbit import random
import speech
import random

location = random.choice(["einem Kiesel", "einer Wiese", "dem Zwiesel"])
action = random.choice(["sass", "stand", "lag", "schlief"])
subj = (["Wiesel"])
prop = random.choice(["Bachgeriesel", "Schneegriesel",
                     "einer Pfuetze Diesel"])
clue = random.choice(["das Mondkalb", "der Nachtalb"])
attitude = random.choice(["um des Reimes Willen", "um einfach mal zu chillen"])

poem = [
    "Das aesthetische Wiesel frei nach Christian Morgenstern",
    "Ein {}".format(subj),
    "{} auf".format(action),
    "inmitten {}".format(prop),
    "Wisst ihr, weshalb?",
    "{} verriet es mir im Stillen:".format(clue),
    "Das raffinierte Tier tats {}".format(attitude)]
for line in poem:
    speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
    speech.pronounce(line, pitch=100, speed=48, mouth=128, throut=128)
    sleep(500)
