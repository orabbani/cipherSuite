# Basic interface for message input

# string BADPATH
# string BADMESSAGE
# string getInput()
# string getFile()
# string getFile_(path)
# bool isValid(message)

import SYMBOLS as S, pyperclip, os

SYMBOLS = S.GET()
BADPATH = 'ERROR: Bad Path'
BADMESSAGE = 'ERROR: Bad Message'

# Prompts for input, validates returns a string (message)
def getInput():
    # Asks if the user wants to paste from clipboard
    i = input('Paste from clipboard? [y/N]').lower()
    if i == 'y':
        paste = True
    else:
        paste = False

    # Either pastes from clipboard or asks for a string
    if paste:
        message = pyperclip.paste()
        print('\nPasted message:\n%s\n' % (message))
    else:
        message = input('Input string to be processed: ')

    # Validates and returns message if isValid returns true
    if isValid(message):
        return message
    else:
        return ''
# END getInput

# Prompts for a path and returns a string(message)
def getFile():
    # Asks for a file path and returns an empty string if invalid
    path = input('File to be encrypted: ')
    if not os.path.exists(path):
        return BADPATH

    # Read the file and return a string
    file = open(path)
    message = file.read()
    file.close()

    if isValid(message):
        return message
    else:
        return BADMESSAGE
# END getFile

# Gets file without path validation
def getFile_(path):
    file = open(path)
    message = file.read()
    file.close()

    if isValid(message):
        return message
    else:
        return BADMESSAGE
# END getFile

# Validates the string (message) and returns a bool (valid)
def isValid(message):
    for symbol in message:
        if symbol not in SYMBOLS:
            return False
    return True
# END validate
