import sys
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
import paths
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
import paths
import cipherSuite
import caesarCipher as cc 
import transpositionCipher as tc
import message as me
import pyperclip as pc
import os
import sys
import detectWords as dw

testResults = cipherSuite.path['testResults']

def test():
    message = me.getFile_('%stest.txt' % (testResults))
    
    ccKey = cc.getKey()
    message = cc.encrypt(message, ccKey)
    print('Encrypted message using caesarCipher. Key: %s' % (ccKey))
    
    tcKey = tc.getKey(message)
    message = tc.encrypt(message, tcKey)
    print('Encrypted message using transpositionCipher. Key: %s' % (tcKey))

    if input('Print encrypted message? [Y/n]: ') != 'n': print('Encrypted message:\n\n%s\n' % (message))
    if input('Write encrypted message to file? [Y/n]: ') != 'n':
        outfile = open('%stest.encrypted.txt' % (testResults), 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote encrypted message to file')

    infile = open('%stest.encrypted.txt' % (testResults))
    message = infile.read()
    infile.close()

    message = tc.decrypt(message, tcKey)
    print('Decrypted message using transpositionCipher')

    message = cc.decrypt(message, ccKey)
    print('Decrypted message using caesarCipher')

    if input('Print decrypted message? [Y/n]: ') != 'n': print('Decrypted message:\n\n%s\n' % (message))
    if input('Write decrypted message to file? [Y/n]: ') != 'n':
        outfile = open('%stest.decrypted.txt' % (testResults), 'w')
        outfile.write(message)
        outfile.close()
        print('Wrote decrypted message to file')

if __name__ == '__main__':
    test()
