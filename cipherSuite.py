sys.path.insert(0, 'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
# 1. paths first so cipherSuite can find everything
import paths
# 2. python modules
import sys, os
# 3rd party modules
import pyperclip
# symbols is a base dependency
import symbols # get()
# message is necessary for ciphers
import message as me # getInput, getFile(), getFile_(path), isValid(message)
# ciphers here. doesn't matter for now what order they're in
import caesarCipher as cc # getKey(), encrypt(message, key), decrypt(message, key)
import transpositionCipher as tc # getKey(message), encrypt(message, key), decrypt(message, key)
# this is a utility and hasn't been implemented yet
import detectWords as dw # isValid(message, wordPercentage, lettersPercentage)

if __name__ == '__main__':
    print('Cipher Suite') 
