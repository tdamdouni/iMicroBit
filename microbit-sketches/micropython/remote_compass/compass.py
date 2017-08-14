import radio
from microbit import display, Image, compass, button_a, button_b, sleep

def send_direction():
    """
    Send the direction which the probe is pointing to:
    direction_N, direction_NE, direction_E...
    """
    display.show(Image.ARROW_N)

    while True:
        sleep(100)
        if button_b.is_pressed():
            break # Back to the menu mode
        heading = compass.heading()
        if (heading > 337) or (heading <= 22):
            needle = "N"
        elif 22 < heading <= 67:
            needle = "NE"
        elif 67 < heading <= 112:
            needle = "E"
        elif 112 < heading <= 157:
            needle = "SE"
        elif 157 < heading <= 202:
            needle = "S"
        elif 202 < heading <= 247:
            needle = "SW"
        elif 257 < heading <= 292:
            needle = "W"
        elif 292 < heading <= 337:
            needle = "W"
        radio.send("dir_{}".format(needle))

def menu_mode():
    """
    Principal menu mode
    """
    while True:
        display.show(Image.HAPPY)
        radio.send("ready")

        if button_a.is_pressed():
            send_direction()

if __name__ == "__main__":
    radio.on()
    compass.calibrate()
    menu_mode()
