import caesarCipher as cc 
import transpositionCipher as tc
import message as me
import pyperclip as pc
import os
import sys
import detectWords as dw

def test_ciphers():
    message = me.getFile_('./test/test.txt')
    print('Got message from ./test/test.txt')
    
    ccKey = cc.getKey()
    message = cc.encrypt(message, ccKey)
    print('Encrypted message using caesarCipher. Key: %s' % (ccKey))
    
    tcKey = tc.getKey(message)
    message = tc.encrypt(message, tcKey)
    print('Encrypted message using transpositionCipher. Key: %s' % (tcKey))

    if input('Print encrypted message? [Y/n]: ') != 'n': print('\nEncrypted message:\n\n%s\n' % (message))
    if input('Write encrypted message to file? [Y/n]: ') != 'n':
        outfile = open('./test/test.encrypted.txt', 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote encrypted message to ./test/test.encrypted.txt')

    infile = open('./test/test.encrypted.txt')
    message = infile.read()
    infile.close()
    print('\nGot message from ./test/test.encrypted.txt')

    message = tc.decrypt(message, tcKey)
    print('Decrypted message using transpositionCipher')

    message = cc.decrypt(message, ccKey)
    print('Decrypted message using caesarCipher')

    if input('Print decrypted message? [Y/n]: ') != 'n': print('\nDecrypted message:\n\n%s\n' % (message))
    if input('Write decrypted message to file? [Y/n]: ') != 'n':
        outfile = open('./test/test.decrypted.txt', 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote decrypted message to ./test.decrypted.txt')

if __name__ == '__main__':
    test_ciphers()
