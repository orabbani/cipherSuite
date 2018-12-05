# int getKey(), string encrypt(message, key), string decrypt(message, key)
import caesarCipher as cc 
# int getKey(message), string encrypt(message, key), string decrypt(message, key)
import transpositionCipher as tc
# string getInput(), string getFile(), string getFile_(path),bool isValid(message), string BADPATH, string BADMESSAGE
import message as me
# copy(), string paste()
import pyperclip as pc
# string GET(), void SET(symbols)
import SYMBOLS as S
# bool path.exists(path)
import os
# exit()
import sys
# string GET(), void SET(path)
import PATH as P
# bool isEnglish(message)
import detectEnglish as de

# Encrypts a given file using random keys and writes to encrypted.txt
def test_ciphers():
    message = me.getFile_('test.txt')
    print('Got message from ./test.txt')
    
    ccKey = cc.getKey()
    message = cc.encrypt(message, ccKey)
    print('Encrypted message using caesarCipher. Key: %s' % (ccKey))
    
    tcKey = tc.getKey(message)
    message = tc.encrypt(message, tcKey)
    print('Encrypted message using transpositionCipher. Key: %s' % (tcKey))

    if input('Print encrypted message? [Y/n]: ') != 'n': print('\nEncrypted message:\n\n%s\n' % (message))
    if input('Write encrypted message to file? [Y/n]: ') != 'n':
        outfile = open('test.encrypted.txt', 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote encrypted message to ./test.encrypted.txt')

    infile = open('test.encrypted.txt')
    message = infile.read()
    infile.close()
    print('\nGot message from ./test.encrypted.txt')

    message = tc.decrypt(message, tcKey)
    print('Decrypted message using transpositionCipher')

    message = cc.decrypt(message, ccKey)
    print('Decrypted message using caesarCipher')

    if input('Print decrypted message? [Y/n]: ') != 'n': print('\nDecrypted message:\n\n%s\n' % (message))
    if input('Write decrypted message to file? [Y/n]: ') != 'n':
        outfile = open('test.decrypted.txt', 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote decrypted message to ./test.decrypted.txt')

if __name__ == '__main__':
    test_ciphers()
