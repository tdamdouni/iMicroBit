
def cypher(message, key):
    # start with an empty result string
    result = ""
    # process each character in the message, one at a time
    for ch in message:
        # converting a character to it's ASCII number
        #   ord() gets the ASCII ordinal value of this character. so 'A' will be 65
        #   see ASCII chart at: http://sticksandstones.kstrom.com/appen.html
        #
        # XOR'in the bits
        #   ^ is XOR, which processes each bit in the character against each bit in key
        #   Truth table for XOR is:
        #   A B   output
        #   0 0   0
        #   0 1   1
        #   1 0   1
        #   1 1   0
        #   XOR is 'exclusive OR' - exclusively one or the other, not both.
        #   Treat column A as the bit in the character
        #   Treat column B as the bit in the key
        #   XOR them together
        #
        # So, think of it like this, if the key bit is '1' it toggles what
        # is already in the character bit.
        #
        # the result is then finally turned from a number back to a character with chr()
        #
        # WORKED EXAMPLE
        # work through each column of bits one at a time...
        #   assuming a key of hex 2A
        #     'G'        ASCII 071   binary 0100 0111
        #     key        HEX   2A    binary 0010 1010
        #     encrypted  char 'm'    binary 0110 1101

        ch = chr(ord(ch) ^ key)
        # append the encrypted character to the end of result string
        result += ch

    # return the result to the code that 'called' this cypher function
    return result

def run():
    # get a string message from the user
    plaintext = input("message? ")

    # get a hex key (preferably in range 00..FF)
    # this will be used to 'mask' over each letter of the message
    key = input("hex number for key? ")
    # parse the 'key' string into an 'int' number, assuming base 16 (hex)
    key = int(key, 16)

    # pass the plaintext and the key to the cypher algorithm
    # what comes back is the cyphered version of plaintext
    cyphertext = cypher(plaintext, key)

    print(cyphertext)
