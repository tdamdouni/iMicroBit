from microbit import *
import radio


def microbit_read_UART():
    response_string = ""
    display.set_pixel(2, 2, 5)
    for i in range(100):
        sleep(100)
        if uart.any():
            response_string = uart.readline()
            break
    display.set_pixel(2, 2, 0)
    return response_string


def microbit_write_UART():
    uart.write("--- connected ---")
    uart.write("\r\n")


def SerialInit():
    sleep(500)
    uart.init(57600)            # do not set any pins when USB connected
    sleep(500)


# Start Here
radio.on()
radio.config(channel=43, queue=10, power=7, length=128, data_rate=radio.RATE_2MBIT)
SerialInit()
sleep(2000)
microbit_write_UART()
display.show(Image.DIAMOND_SMALL)
wait_4_send = 0


while True:
    if wait_4_send == 0:
        Message = microbit_read_UART()

    if Message and wait_4_send == 0:
        uart.write("ready to send... press button A to transmit, B to clear")
        uart.write("\r\n")
        uart.write(Message)       # echo while using the FTDI
        uart.write("\r\n")
        display.show(Image.BUTTERFLY)
        wait_4_send = 1

    if button_a.is_pressed():
        wait_4_send = 2
        display.clear()

    if wait_4_send == 2:           # and button_a.was_pressed():
        uart.write("... sending")
        uart.write("\r\n")
        radio.send_bytes(Message)
        display.show(Image.HAPPY)
        sleep(2000)
        Message = ""
        display.clear()
        wait_4_send = 0

    if button_b.is_pressed() and wait_4_send == 1:
        Message = ""
        uart.write("... message cleared. enter a new one")
        uart.write("\r\n")
        display.clear()
        wait_4_send = 0
