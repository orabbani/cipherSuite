sys.path.insert(0, 'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
# Simple Caesar Cipher encryption/decryption

# int getKey()
# string encrypt(message, key)
# string decrypt(message, key)

import random, symbols

BAD_INPUT = 'Bad input. Try agian'
SYMBOLS = symbols.get()
KEY_LIMIT = len(SYMBOLS)

# Generates and returns an int (key)
def getKey():
    return random.randint(1, KEY_LIMIT - 1)
# END getKey function  

# Encrypts string (message) using int (key), returns string (translation)
def encrypt(message, key):
    translation = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex + key
        if translatedIndex >= KEY_LIMIT:
            translatedIndex -= KEY_LIMIT
        translation += SYMBOLS[translatedIndex]

    return translation
# END encrypt

# Decrypts string (message) using int (key), returns string (translation)
def decrypt(message, key):
    translation = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex - key
        if translatedIndex < 0:
            translatedIndex += KEY_LIMIT
        translation += SYMBOLS[translatedIndex]

    return translation
# END decrypt

