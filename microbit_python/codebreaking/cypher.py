# cypher.py - encrypt and decrypt messages

def cypher(message, key):
    result = ""
    for ch in message:
        ch = chr(ord(ch) ^ key)
        result += ch
    return result

def run():
    plaintext = input("message? ")
    key = input("hex number for key? ")
    key = int(key, 16)

    cyphertext = cypher(plaintext, key)
    print(cyphertext)
