import sys
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
import paths
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
sys.path.insert(0, 'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
# Simple transposition cipher encryption/decryption

# int getKey(message)
# string encrypt(message, key)
# string decrypt(message, key)

import math, random

# Generates and returns an int (key)
def getKey(message):
    return random.randint(1, (math.floor(len(message) / 2)))
# END getKey

# Encrypts string (message) using int (key), returns string (translation)
def encrypt(message, key):
    translation = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            translation[column] += message[currentIndex]
            currentIndex += key

    return ''.join(translation)
# END encrypt

# Decrypts string (message) using int (key), returns string (translation)
def decrypt(message, key):
    columns = int(math.ceil(len(message) / float(key)))
    rows = key
    shadows = (columns * rows) - len(message)
    translation = [''] * columns

    column = 0
    row = 0

    for symbol in message:
        translation[column] += symbol
        column += 1

        if (column == columns) or (column == columns - 1 and row >= rows - shadows):
            column = 0
            row += 1

    return ''.join(translation)
# END decrypt
