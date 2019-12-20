# cipherSuite.py
# Author: slinkyfromhell
# Description:
#   Classes and methods pertaining to simple cipher techniques.
#   Only provides minimal input validation. A bad key will result
#       in an object not instantiating correctly. It is recommended
#       to allow the library to generate a key upon encryption, and to
#       use <Cipher>.getKey() to retrieve it for decryption.

# Example usage:
'''
* One liner - print translation:
    print(Caesar(message='test message', key=42, mode='e').translation)
* Intended usage:
    c = Caesar(message, mode='e')
    k = c.getKey()
    t = c.translation
* Additional parameters:
    Caesar(message, key, mode)
    modes = {
        'e':'encrypt',
        'd':'decrypt'
    }

----- Disabling bad key verbosity -----  
* Caesar:
    c = Caesar()
    c.key = c.Key(key=key, v=False)
* Transposition:
    c = Transposition(message=message)
    c.key = c.Key(message=message, key=key, v=False)
'''

# Import standard libraries
import sys, os, secrets, string, math
# Append lib directory path to system path
lib_path = os.path.join(os.getcwd(),'lib')
sys.path.insert(0, lib_path)
# Import additional libraries
import pyperclip # pyperclip.copy(var) || var = pyperclip.paste()

CHARSET = string.ascii_letters + string.digits + string.punctuation + string.whitespace

class Caesar:
    class Key:
        # Random key generator
        def generate(self):
            self.set(secrets.randbelow(self.limit-1) + 1)
        # Key variable I/O
        def print(self): print('KEY_CAE:', self.key)
        def get(self): return self.key
        # If keyVal is valid returns 1, else returns 0
        def set(self, keyVal):
            if keyVal <= self.limit and keyVal > 0:
                self.key = keyVal
                return 1
            else: return 0

        def __init__(self, key=None, v=True):
            # Set the upper value limit for the key
            self.limit = len(CHARSET)
            # Check if key var was passed
            if key:
                # Passes to set. Does nothing if accepted
                if self.set(key) == 1: None
                # If key was out of bounds, generate a new key and print
                else:
                    if v: print('ERR_CAE: Bad key given. Generating a new one')
                    self.generate()
                    if v: self.print()
            # If var was not passed, generate a key
            else: self.generate()

    # Access Key variables
    def getKey(self): return self.key.get()
    def setKey(self, key): self.key.set(key)
    def getKeyLimit(self): return self.key.limit

    # Encrypts the message and sets Caesar.translation
    def encrypt(self):
        translation = ''
        for c in self.message:
            charIndex = CHARSET.find(c)
            translatedIndex = charIndex + self.getKey()
            if translatedIndex >= self.getKeyLimit():
                translatedIndex -= self.getKeyLimit()
            translation += CHARSET[translatedIndex]
        self.translation = translation

    # Decrypts the message and sets Caesar.translation
    def decrypt(self):
        translation = ''
        for c in self.message:
            charIndex = CHARSET.find(c)
            translatedIndex = charIndex - self.getKey()
            if translatedIndex < 0:
                translatedIndex += self.getKeyLimit()
            translation += CHARSET[translatedIndex]
        self.translation = translation

    def __init__(self, message=None, key=None, mode=None):
        if message: self.message = message
        if key: self.key = self.Key(key)
        else: self.key = self.Key()
        if mode:
            if mode == 'e':
                if not message: print('ERR_CAE_INIT: No message given.')
                else: self.encrypt()
            elif mode == 'd':
                if not message: print('ERR_CAE_INIT: No message given.')
                elif not key: print('ERR_CAE_INTI: No key given.')
                else: self.decrypt()
            else: print('ERR_CAE_INIT: Invalid mode given.')


class Transposition:
    class Key:
        def generate(self, message):
            self.key = secrets.randbelow(self.limit) + 2
            while self.key > self.limit: self.key -= 1

        def print(self): print('KEY_TRA:', self.key)

        def get(self): return self.key
        def set(self, key):
            if key > 2 and key < self.limit:
                self.key = key
                return 1
            else: return 0
 
        def __init__(self, message, key=None, v=True):
            self.limit = math.floor(len(message) / 2)
            if key:
                # Passes to set. Does nothing if accepted
                if self.set(key) == 1: None
                # If key was out of bounds, generate a new key and print
                else:
                    if v: print('ERR_TRA_INIT: Bad key given. Generating a new one')
                    self.generate(message)
                    if v: self.print()
            # If var was not passed, generate a key
            else: self.generate(message)

    def getKey(self): return self.key.get()
    def setKey(self, key): self.key.set(key)
    def getKeyLimit(self): return self.key.limit

    def encrypt(self):
        if not self.message:
            print('ERR_TRA_ENC: no value assigned to Transposition.message')
        if not self.key: self.key = self.Key(self.message)
        translation = [''] * self.getKey()
        for column in range(self.getKey()):
            index = column
            while index < len(self.message):
                translation[column] += self.message[index]
                index += self.getKey()
        self.translation = ''.join(translation)

    def decrypt(self):
        columns = int(math.ceil(len(self.message) / float(self.getKey())))
        rows = self.getKey()
        shadows = (columns * rows) - len(self.message)
        translation = [''] * columns
        column = 0
        row = 0
        for c in self.message:
            translation[column] += c
            column += 1
            if (column == columns) or \
                (column == columns - 1 and row >= rows - shadows):
                column = 0
                row += 1
        self.translation = ''.join(translation)

    def __init__(self, message, key=None, mode=None):
        if message:
            self.message = message
            if key: self.key = self.Key(message=message, key=key)
            else: self.key = self.Key(message=message)
        
        if mode:
            if mode == 'e':
                if not message: print('ERR_CAE_INIT: No message given.')
                else: self.encrypt()
            elif mode == 'd':
                if not message: print('ERR_CAE_INIT: No message given.')
                elif not key: print('ERR_CAE_INTI: No key given.')
                else: self.decrypt()
            else: print('ERR_CAE_INIT: Invalid mode given.')


class Key:
    def join_keys(self, ciphers):
        key = ''
        for cipher in ciphers:
            cName = cipher.__class__.__name__[:3].lower()
            key += cName + str(cipher.getKey())
        self.key = key

    def parse_key(self, key): None

    def __init__(self, ciphers=None, key=None, mode=None):
        if ciphers: 
            self.ciphers = ciphers
            if mode:
                if mode == 'j': self.join_keys(ciphers)
                if mode == 'p': self.parse_key(key)


def test_all():
    print('=========== Encryption ===========')
    print('==== Transposition ====')
    tMsg = 'This is a test string!'
    t = Transposition(message=tMsg, mode='e')
    tCrypt = t.translation
    tKey = t.getKey()
    print('msg:',tMsg)
    print('crypt:',tCrypt)
    print('key:',tKey)

    print('==== Caesar ====')
    cMsg = tCrypt
    c = Caesar(message=cMsg, mode='e')
    cCrypt = c.translation
    cKey = c.getKey()
    print('msg:',cMsg)
    print('crypt:',cCrypt)
    print('key:',cKey)

    print('=========== Decryption ===========')
    print('==== Caesar ====')
    c = Caesar(message=cCrypt, key=cKey, mode='d')
    cDCrypt = c.translation
    print('dCrypt:',cDCrypt)

    print('==== Transposition ====')
    tCrypt = cDCrypt
    t = Transposition(message=tCrypt, key=tKey, mode='d')
    tDCrypt = t.translation
    print('dCrypt:',tDCrypt)
    
    print('=========== Keys ===========')
    print('==== Joining ====')
    #print(join_keys([c, t]))

def test_caesar(): None
def test_Transposition(): None


if __name__=='__main__':
    test_all()
