from microbit import display, button_a, button_b, sleep
import radio

radio.on()
radio.config(channel=86)


def output(data):
    radio.send(str(data))
    data = str(data)
    if len(data) == 1:
        display.show(data)
    else:
        display.scroll(data)


def inc_num(num):
    num += 1
    output(num)
    return num


def change_op(operator):
    if operator == "ADD":
        operator = "MIN"
    elif operator == "MIN":
        operator = "MUL"
    elif operator == "MUL":
        operator = "DIV"
    elif operator == "DIV":
        operator = "ADD"
    output(operators[operator])
    return operator
sleep_time = 125
total = 0
num = 0
operator = "ADD"
operators = {
        "ADD": "+",
        "MIN": "-",
        "MUL": "x",
        "DIV": "/"
            }
while True:
    if button_a.is_pressed():
        num = inc_num(num)
    elif button_b.is_pressed():
        if num != 0:
            if operator == "ADD":
                total += num
            elif operator == "MIN":
                total -= num
            elif operator == "MUL":
                total *= num
            elif operator == "DIV":
                total /= num
            num = 0
            output(total)
        else:
            operator = change_op(operator)
    sleep(sleep_time)
