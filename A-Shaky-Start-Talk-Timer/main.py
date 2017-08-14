#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A Timer for the MicroBit"""
from microbit import display, accelerometer, sleep, button_a, button_b, running_time, Image
import radio

# A Staky Start Talk Time

SHAKY_ID = 'asstt'


def start_up_screen():
    """Display the start up screen"""
    display.show(Image.ALL_CLOCKS, delay=100, loop=False, clear=True)
    return


def show_power_on():
    """Display power on configuration"""
    display.set_pixel(0, 0, 9)
    return


def clear_message_buffer():
    """Wait until radio buffer is clear"""
    while radio.receive() is not None:
        pass
    return


def wait_till_shaking_stops():
    """Wait until shaking stops"""
    while accelerometer.current_gesture() == 'shake':
        pass
    return


def get_ready_to_go_again():
    """Reset Timer"""
    clear_message_buffer()
    wait_till_shaking_stops()
    return


def count_down(delay):
    """Count down and show progress"""
    on_image = Image('99999:99999:99999:99999:99999')
    display.show(on_image)

    for y_coord in range(5):
        for x_coord in range(5):
            wait = delay
            while wait >= 300:
                sleep(300)
                wait -= 300
                if abandon_talk() is True:
                    return

                # Flash the last row, so making it clear that
                # the talk is coming to an end

                if y_coord == 4:
                    for i in range(x_coord, 5):
                        brightness = display.get_pixel(i, y_coord)
                        if brightness == 0:
                            brightness = 9
                        else:
                            brightness = 0
                        display.set_pixel(i, y_coord, brightness)

            sleep(wait)
            display.set_pixel(x_coord, y_coord, 0)

    start_up_screen()
    return


def display_minutes(minutes):
    """Show minutes"""
    i = 0
    for y_coord in range(5):
        for x_coord in range(5):
            i += 1
            if i <= minutes:
                display.set_pixel(x_coord, y_coord, 9)
            else:
                if x_coord == 0 and y_coord == 0 and minutes < 1:
                    display.set_pixel(x_coord, y_coord, 4)
                else:
                    display.set_pixel(x_coord, y_coord, 0)


def get_talk_time(minutes):
    """Setup talk time"""
    display.scroll('A -1, B +1')

    # clear press counters

    button_a.get_presses()
    button_b.get_presses()

    quit_flag = False

    while quit_flag is not True:
        minutes = minutes - button_a.get_presses() \
            + button_b.get_presses()
        display_minutes(int(minutes))

        # To exit press a for 2 seconds

        if button_a.is_pressed():
            start = running_time()

            while button_a.is_pressed():
                if running_time() - start > 2000:
                    quit_flag = True
                    display.scroll(str(int(minutes)))

    return minutes


def minutes_to_delay(minutes):
    """Compute delay from minutes"""
    return minutes * 60 * 1000 / 25


def delay_to_minutes(delay):
    """Compute minutes from delay"""
    return delay * 25 / (60 * 1000)


def message_to_delay(receivedmess):
    """Get delay from radio"""
    if receivedmess is not None:
        (asstdev, started, remotetime) = receivedmess.split()

        if asstdev == SHAKY_ID and started == 'start':
            return float(remotetime)

    return -1


def abandon_talk():
    """Abandon talk"""
    if button_a.is_pressed():
        radio.send(SHAKY_ID + ' ' + 'stop')
        display.show(Image.SKULL)
        while button_a.is_pressed():
            pass
        return True

    receivedmess = radio.receive()
    if receivedmess is not None:
        try:
            (asstdev, stopped) = receivedmess.split()
        except ValueError:
            return False

        if asstdev == SHAKY_ID and stopped == 'stop':
            return True

    return False


def main():
    """Main function for the timer"""

    # set the number minutes that your talk is to last for.
    minutes = 1

    # convert to the delay needed to turn off each LED
    delay = minutes_to_delay(minutes)

    start_up_screen()
    show_power_on()

    radio.on()

    while True:

        received_message = radio.receive()

        delay_from_remote = message_to_delay(received_message)

        if delay_from_remote >= 0:
            delay = delay_from_remote
            count_down(delay)
            get_ready_to_go_again()

        # Show number of mins

        display_minutes(delay_to_minutes(delay))

        # To enter demo mode press button a for > 2 secs

        if button_b.is_pressed():
            start = running_time()

            while button_b.is_pressed():
                pass

            if running_time() - start > 2000:
                delay = minutes_to_delay(15 / 60)
                display.scroll('Talk 15 secs')

        if button_a.is_pressed():
            delay = minutes_to_delay(get_talk_time(delay_to_minutes(delay)))
            start_up_screen()
            display_minutes(delay_to_minutes(delay))

        if accelerometer.current_gesture() == 'shake':
            send_message = True
            while accelerometer.current_gesture() == 'shake':
                delay_from_remote = message_to_delay(received_message)
                if delay_from_remote >= 0:
                    delay = delay_from_remote
                    send_message = False

            if send_message:
                radio.send(SHAKY_ID + ' ' + 'start ' + str(delay))

            count_down(delay)
            get_ready_to_go_again()


if __name__ == "__main__":
    main()
