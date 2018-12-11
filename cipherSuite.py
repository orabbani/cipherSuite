import sys, os
import paths

# Third party modules
import pyperclip

# symbols is a base dependency and should go early in the load order
import symbols # get()
SYMBOLS = symbols.get()

# message is necessary for ciphers
import message as me # getInput(), getFile(), getFile_(path), isValid(message)

# ciphers here. doesn't matter for now what order they're in
import caesarCipher as cc # getKey(), encrypt(message, key), decrypt(message, key)
import transpositionCipher as tc # getKey(message), encrypt(message, key), decrypt(message, key)

# this is a utility and hasn't been implemented yet
import detectWords as dw # isValid(message, wordPercentage, lettersPercentage)









def test():
    print('test')

if __name__ == '__main__':
    print('Cipher Suite') 
