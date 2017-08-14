from microbit import display, button_a, button_b, sleep, accelerometer
import radio

radio.on()
radio.config(channel=86)


def output(data):
    radio.send(str(data))
    data = str(data)
    if len(data) == 1:
        if data == "*":
            data = "x"
        display.show(data)
    else:
        display.scroll(data)


def inc_num(num):
    if int(str(num)[-1]) >= 9:
        if len(str(num)) == 1:
            num = 0
        else:
            num = int(str(num)[:-1]+"0")
    else:
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
operator = "ADD"
num = 0
operators = {
        "ADD": "+",
        "MIN": "-",
        "MUL": "*",
        "DIV": "/"
            }
btn = "A"
while True:
    if accelerometer.was_gesture("shake") and num != 0:
        btn = "S"
        total = eval(str(total)+operators[operator]+str(num))
        operator = "ADD"
        num = 0
        output(total)
        
    elif button_a.is_pressed():
        if btn == "B":
            btn = "A"
            num *= 10
            output(num)
        elif btn == "A":
            num = inc_num(num)
        elif btn == "S":
            operator = change_op(operator)
        sleep(2*sleep_time)
    elif button_b.is_pressed():
        if btn == "A":
            btn = "B"
            num *= 10
            output(num)
        elif btn == "B":
            num = inc_num(num)
        elif btn == "S":
            
            btn = "B"
        sleep(2*sleep_time)
