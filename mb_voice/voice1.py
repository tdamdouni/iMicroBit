# voice1.py  20/06/2016  D.J.Whale
#
# A simple Stephen Hawking Box, using the micro:bit.

import microbit

phrases = [
# A-E
"thanks",
"please",
"awesome",
"i see",
"sorry",

# F-J
"yes",
"no",
"dont know",
"not sure",
"definitely",

# K-O
"hows it going",
"how could you improve it",
"what else",
"what have you tried",
"what is next",

# P-T
"when i say go",
"go",
"5 minutes left",
"2 minutes left",
"stop",

# U-Y
"quiet please",
"hello",
"my name is david",
"i have lost my voice",
"i am a software engineer",

# Z
None # reserved as a trigger to change palettes
]

def say(phrase):
    print(phrase)
    import os
    os.system("say %s" % phrase)


try:
    readin = raw_input # python 2
except NameError :
    readin = input # python 3


while True:
    ##p = readin("phrase letter A-Z? ")
    p = microbit.get()

    pi = (p[0]).upper()
    if pi < 'A' or pi > 'Z':
        print("Must choose A-Z")
        continue

    index = ord(pi) - 65
    phrase = phrases[index]
    if phrase == None:
        print("Placeholder for phrasebook switching")
    else:
        say(phrase)
