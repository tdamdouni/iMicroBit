import microbit
import random
import radio
import music

def flicker(time):
    if time < 1000:
        time = 1000
    pause = 100
    loops = time / 250;
    for i in range(loops):
        for x in range(5):
            for y in range(5):
                value = int(random.randint(0, 9) * (1 - (i - 1) / loops))
                microbit.display.set_pixel(x, y, value)
        microbit.sleep(pause)
    microbit.display.clear()

radio.on()

while True:
    if microbit.button_a.was_pressed():
        radio.send('flash')
        flicker(3200)
    if microbit.button_b.was_pressed():
        radio.send('smile')
        microbit.display.show(microbit.Image.ASLEEP)
        music.play(music.POWER_DOWN)
        microbit.sleep(1000)
        microbit.display.clear()

    incoming = radio.receive()
    if incoming == 'flash':
        flicker(3200)
    if incoming == 'smile':
        microbit.display.show(microbit.Image.HAPPY)
        music.play(music.POWER_UP)
        microbit.sleep(1000)
        microbit.display.clear()
