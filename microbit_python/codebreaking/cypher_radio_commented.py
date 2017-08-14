# cypher_radio.py - encrypt and decrypt messages over radio

from microbit import *
import radio
radio.config() # you can change frequency and bit rate in here if you want to

def cypher(message, key):
    # see comments in cypher_commented.oy
    result = ""
    for ch in message:
        ch = chr(ord(ch) ^ key)
        result += ch
    return result

def send():
    # get a message and a key from the user
    plaintext = input("message? ")
    key = input("hex number for key? ")
    key = int(key, 16)

    # encrypt plaintext with key to create cyphertext
    cyphertext = cypher(plaintext, key)

    # turn radio on ready for transmit
    radio.on()
    # transmit the encrypted message 10 times
    for i in range(10):
        print(i, cyphertext) # print on our REPL console so we can see it too
        radio.send(cyphertext)
        sleep(100) # don't send too fast, might corrupt the data

    # turn the radio off when we have finished with it
    radio.off()
    
def receive():
    # get the key from the user
    # this must be the same as the key used by the transmitter,
    # otherwise it will look like garbage
    key = input("hex number for key? ")
    key = int(key, 16)

    # turn the radio on so we can receive radio packets
    radio.on()

    while True:
        try:
            # try to receive another message
            cyphertext = radio.receive()
            # radio.receive is non-blocking, it will return None if no message waiting
            if cyphertext is not None:
                # we got a message, decrypt cyphertext with key to create plaintext
                plaintext = cypher(cyphertext, key)
                # display the plaintext message to the user
                print(plaintext)
        except:
            # there is a bug in MicroPython
            # if you get a corrupted packet of data, it locks the radio up
            # turning the radio off then on again recovers it.
            radio.off()
            radio.on()

def help():
    print("try send() or receive()")
