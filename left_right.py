from microbit import *
import random

timeAllowed = 500
time = 0

while True:
    display.show(Image("00000:00100:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00200:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00300:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00400:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00500:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00600:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00700:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00800:00000:00000:00000"))
    sleep(100)
    display.show(Image("00000:00900:00000:00000:00000"))
    sleep(100)
    display.show(Image("00900:09090:00900:00000:00000"))
    sleep(100)
    display.show(Image("09090:90009:09090:00000:00000"))
    sleep(100)

    rightImage = Image(
        "00090:"
        "00009:"
        "00090:"
        "00000:"
        "00000"
    )

    leftImage = Image(
        "09000:"
        "90000:"
        "09000:"
        "00000:"
        "00000"
    )

    display.show(leftImage + rightImage)
    while True:
        if button_b.is_pressed() and button_a.is_pressed():
            break

    display.show("3")
    sleep(1000)
    display.show("2")
    sleep(1000)
    display.show("1")
    sleep(1000)

    if random.randint(1, 2) == 1:
        direction = "left"
        image = leftImage
    else:
        direction = "right"
        image = rightImage

    display.show(image)

    score = 0

    while True:
        if direction == "left":
            if button_b.is_pressed():
                display.show(Image.NO)
                break
            elif button_a.is_pressed():
                if timeAllowed > 10:
                    timeAllowed = timeAllowed - 10

                score = score + 1
                display.clear()
                sleep(500)

                image.set_pixel(0, 4, 0)
                image.set_pixel(1, 4, 0)
                image.set_pixel(2, 4, 0)
                image.set_pixel(3, 4, 0)
                image.set_pixel(4, 4, 0)

                if random.randint(1, 2) == 1:
                    direction = "left"
                    image = leftImage
                else:
                    direction = "right"
                    image = rightImage

                display.show(image)
                time = 0

        else:
            if button_a.is_pressed():
                display.show(Image.NO)
                break
            elif button_b.is_pressed():
                if timeAllowed > 10:
                    timeAllowed = timeAllowed - 10

                score = score + 1
                display.clear()
                sleep(500)

                image.set_pixel(0, 4, 0)
                image.set_pixel(1, 4, 0)
                image.set_pixel(2, 4, 0)
                image.set_pixel(3, 4, 0)
                image.set_pixel(4, 4, 0)

                if random.randint(1, 2) == 1:
                    direction = "left"
                    image = leftImage
                else:
                    direction = "right"
                    image = rightImage

                display.show(image)
                time = 0

        sleep(1)
        time = time + 1

        if (time/timeAllowed) > 0.25:
            image.set_pixel(2, 4, 9)
            display.show(image)

        if (time/timeAllowed) > 0.50:
            image.set_pixel(1, 4, 9)
            image.set_pixel(3, 4, 9)
            display.show(image)

        if (time/timeAllowed) > 0.75:
            image.set_pixel(0, 4, 9)
            image.set_pixel(4, 4, 9)
            display.show(image)

            if time > timeAllowed:
                display.show(Image.NO)
                break

    sleep(1000)
    display.scroll("SCORE: " + str(score) + "   ")
