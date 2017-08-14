from microbit import *
import music
import radio
import speech

radio.on()

PITCH = 440

# PIN2 read_analog()
ACTION_VALUE = 50
VOLUMEUP_VALUE = 150
VOLUMEDOWN_VALUE = 350
#nothing: 944

def read_buttons():
    v = pin2.read_analog()
    if v < ACTION_VALUE:
        return "action"
    elif v < VOLUMEUP_VALUE:
        return "up" 
    elif v < VOLUMEDOWN_VALUE:
        return "down"
    else:
        return None
        
def run():
    while True:
        display.show(Image.DIAMOND_SMALL)
        try:
            msg = radio.receive()
        except:
            radio.off()
            radio.on()
            msg = None
            
        buttons = read_buttons()
            
        if msg is not None:
            display.show(Image.DIAMOND)
            if buttons == "action":
                speech.say(msg)
            else:
                speech.say("a")
            #    music.pitch(PITCH, pin=pin0)
            #    music.pitch(PITCH, pin=pin1)
            #    sleep(100)
            #    music.stop(pin0)
            #    music.stop(pin1)
            sleep(250) # keep image on display for a bit longer

run()

