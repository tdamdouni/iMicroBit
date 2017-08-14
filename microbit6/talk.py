import microbit
import random
import radio

radio.on()

def listen():
    for i in range(20):
        answer = radio.receive()
        if answer is not None:
            return answer
        microbit.sleep(100)
    return None

def respond(message):
    if message == 'hello':
        radio.send('hey')
        microbit.display.show(microbit.Image.HAPPY)
        microbit.sleep(1000)
        microbit.display.clear()

def start_talking():
    microbit.display.show(microbit.Image.SMILE)
    microbit.sleep(1000)
    radio.send('hello')
    answer = listen()
    if answer == 'hey':
        microbit.display.show(microbit.Image.HAPPY)
    else:
        microbit.display.show(microbit.Image.MEH)

    microbit.sleep(1000)
    microbit.display.clear()

################################################################

last_talk = 0

while True:
    passed_time = microbit.running_time() - last_talk
    if passed_time > 2300 and random.random() < 0.01:
        start_talking()
        last_talk = microbit.running_time()
    else:
        message = radio.receive()
        if message is not None:
            respond(message)
    microbit.sleep(100)
    