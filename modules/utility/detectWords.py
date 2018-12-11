import sys
sys.path.insert(0, r'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
# Detect Words module
def loadDictionary(language):
    file = open('./dictionaries/%s.dic' % (language))
    validWords = {}
    for word in file.read().split('\n'):
        validWords[word] = language     # I set this to have a tag in case I ever want to try implementing new languages
    file.close()
    return validWords

def charset(language):
    file = open('./charsets/%s.char' % (language))
    return file.read().lower() + ' \t\n'

def getValidCount(message, language):
    validWords = loadDictionary(language)
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in validWords:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message, language):
    lettersOnly = []
    for symbol in message:
        if symbol in charset(language):
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isValid(message, wordPercentage=20, lettersPercentage=85):
    wordsMatch = getValidCount(message, language) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message, language))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= lettersPercentage
    return wordsMatch and lettersMatch

