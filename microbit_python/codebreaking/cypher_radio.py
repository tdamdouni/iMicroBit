# cypher_radio.py - encrypt and decrypt messages over radio

from microbit import *
import radio
radio.config()

def cypher(message, key):
    result = ""
    for ch in message:
        ch = chr(ord(ch) ^ key)
        result += ch
    return result

def send():
    plaintext = input("message? ")
    key = input("hex number for key? ")
    key = int(key, 16)

    cyphertext = cypher(plaintext, key)
    radio.on()
    for i in range(10):
        print(i, cyphertext)
        radio.send(cyphertext)
        sleep(100)
    radio.off()
    
def receive():
    key = input("hex number for key? ")
    key = int(key, 16)
     
    radio.on()
    while True:
        try:
            cyphertext = radio.receive()
            if cyphertext is not None:
                plaintext = cypher(cyphertext, key)
                print(plaintext)
        except:
            radio.off()
            radio.on()

def help():
    print("try send() or receive()")
