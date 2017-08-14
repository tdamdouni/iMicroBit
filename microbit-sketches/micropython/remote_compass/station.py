import radio
from microbit import display, Image

def decode_direction(dirstring):
    """
    Decode the dir_X and show the arrow
    """
    needle = dirstring.split("dir_")[1]
    img = getattr(Image, "ARROW_{}".format(needle))
    display.show(img)

if __name__ == "__main__":

    radio.on()

    while True:

        incoming = radio.receive()

        if incoming is None:
            continue

        elif incoming.startswith("dir_"):
            decode_direction(incoming)

        elif incoming == "ready":
            display.show(Image.HAPPY)

