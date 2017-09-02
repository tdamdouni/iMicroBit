from microbit import *
import speech
import music

while True:
    if button_a.is_pressed():
        speech.say("I am a class dee amplif eyer for the micro biht",speed=87)
    if button_b.is_pressed():
        music.play(music.DADADADUM)
    if pin16.read_digital() == 0:
        #music.play(music.POWER_DOWN)
        tune = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8",
        "E:4", "F", "G:8"]
        music.play(tune)
    if pin12.read_digital() == 0:
        music.pitch(4096 - (500+(pin1.read_analog() * 2)),25)