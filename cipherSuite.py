# Import cipher modules
import caesarCipher as cc # getKey(), encrypt(message, key), decrypt(message, key)
import transpositionCipher as tc # getKey(message), encrypt(message, key), decrypt(message, key)

# Import my utility modules
import detectWords as dw # isValid(message, wordPercentage, lettersPercentage)
import message as me # getInput, getFile(), getFile_(path), isValid(message)
import symbols # get()

# Import external modules
import os, sys, pyperclip

path = {}
def setPaths():
    file = open('paths')
    paths = file.read()
    for line in paths.split('\n'):
        word = line.split()
        path[word[0]] = word[1]

def setPath(folderName, folderPath):
    path[folderName] = folderPath

if __name__ == '__main__':
    setPaths()
