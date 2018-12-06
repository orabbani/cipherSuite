# Basic interface for message input

# string getInput()
# string getFile()
# string getFile_(path)
# bool isValid(message)

import pyperclip, os, symbols, reportError

SYMBOLS = symbols.get()
BADPATH = 'ERROR: Bad Path'
BADMESSAGE = 'ERROR: Bad Message'

# Validates and returns message or error
def isValid(message):
    for symbol in message:
        if symbol not in SYMBOLS:
            print('ERROR:SYMBOL_NOT_IN_LIBRARY: %s' % (symbol))
            reportError.invalidSymbol(symbol)
            return BADMESSAGE
    return message
# END isValid

# Function for manual string input
def getInput():
    if input('Paste from clipboard? [y/N]').lower() == 'y':
        message = pyperclip.paste()
        print('\nPasted message:\n%s\n' % (message))
    else:
        message = input('Input string to be processed: ')

    return isValid(message)
# END getInput

# Gets a message in a file without prompting for input
def getFile_(path):
    if not os.path.exists(path):
        print('ERROR:PATH_NOT_FOUND: %s' % (path))
        return BADPATH
    
    file = open(path)
    message = file.read()
    file.close()
    return isValid(message)
# END getFile_

# Prompts for a path and returns a string(message)
def getFile():
    path = input('File to be encrypted: ')
    return getFile_(path)
# END getFile

