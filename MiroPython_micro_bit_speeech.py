import speech
from microbit import sleep

speech.say("I am a little robot",  speed=92, pitch=60, throat=190, mouth=190)
sleep(1000)
speech.say("I am an elf", speed=72, pitch=64, throat=110, mouth=160)
sleep(1000)
speech.say("I am a news presenter", speed=82, pitch=72, throat=110, mouth=105)
sleep(1000)
speech.say("I am an old lady", speed=82, pitch=32, throat=145, mouth=145)
sleep(1000)
speech.say("I am E.T.", speed=100, pitch=64, throat=150, mouth=200)
sleep(1000)
speech.say("I am a DALEK - EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)
