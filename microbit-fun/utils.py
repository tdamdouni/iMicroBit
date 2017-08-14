from microbit import *

NUMBERS = {
    '0': Image('09900:'
          '90090:'
          '90090:'
          '90090:'
          '09900'),
    '1': Image('00900:'
          '09900:'
          '00900:'
          '00900:'
          '09990'),
    '2': Image('09900:'
          '90090:'
          '00900:'
          '09000:'
          '99990'),
    '3': Image('99900:'
          '00090:'
          '09900:'
          '00090:'
          '99900'),
    '4': Image('00900:'
          '09900:'
          '90900:'
          '99990:'
          '00900'),
    '5': Image('99990:'
          '90000:'
          '99900:'
          '00090:'
          '99900'),
    '6': Image('09900:'
          '90000:'
          '99900:'
          '90090:'
          '09900'),
    '7': Image('99990:'
          '00090:'
          '09900:'
          '09000:'
          '90000'),
    '8': Image('09900:'
          '90090:'
          '09900:'
          '90090:'
          '09900'),
    '9': Image('09900:'
          '90090:'
          '09990:'
          '00090:'
          '09900'),
    ':': Image('00000:'
          '00900:'
          '00000:'
          '00900:'
          '00000'),
}


def image_from_number(number):
    """Return an image composed of all the digits of a number."""
    img_width = len(number) * 5
    img = Image(img_width, 5)
    for digit_pos, digit in enumerate(number):
        digit_img = NUMBERS[digit]
        for x in range(5):
            for y in range(5):
                digit_pixel = digit_img.get_pixel(x, y)
                img.set_pixel(x + (digit_pos * 5), y, digit_pixel)
    return img


def zigzag(get_value_func, delay, pause):
    """Scroll a large image left then right to display all of it."""
    img = get_value_func()
    img_width = img.width()
    # 5 less because we already display one "screen".
    pixels_to_scroll = img_width - 5
    for i in range(pixels_to_scroll + 1):
        img = get_value_func()
        display.show(img.shift_left(i))
        sleep(delay)
    sleep(pause)
    for i in range(pixels_to_scroll, -1, -1):
        img = get_value_func()
        display.show(img.shift_left(i))
        sleep(delay)
    sleep(pause)


def blink(img):
    for i in range(5):
        display.show(img)
        sleep(200)
        display.clear()
        sleep(200)
