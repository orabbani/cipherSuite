import sys, os

path = {}
file = open('paths')
paths = file.read()
for line in paths.split('\n'):
    if line[0] != '#': # Allows for commenting ;)
        word = line.split()
        cwd = os.path.dirname(os.path.abspath(__file__))
        fullPath = str(cwd) + word[1]
        path[word[0]] = fullPath            
        sys.path.insert(0, fullPath)

import pyperclip
import detectWords as dw # isValid(message, wordPercentage, lettersPercentage)
import message as me # getInput, getFile(), getFile_(path), isValid(message)
import symbols # get()
import caesarCipher as cc # getKey(), encrypt(message, key), decrypt(message, key)
import transpositionCipher as tc # getKey(message), encrypt(message, key), decrypt(message, key)

if __name__ == '__main__':
    print('Cipher Suite') 
