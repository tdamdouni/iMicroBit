from microbit import display, button_a, Image
import radio
radio.on()
while True:
    message = radio.receive()
    if message:
        display.show(Image.DUCK)
    if button_a.was_pressed():
        display.clear()
        radio.send("hello")
        