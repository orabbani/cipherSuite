import sys
sys.path.insert(0, r'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths

import os, cipherSuite as cs, symbols

def invalidSymbol(symbol):
    file = open(cs.path['errorLog'] + 'invalidSymbols', 'a')
    file.write(symbol)
    file.close()
    print('Trying to add symbol to library...')
    symbols.add(symbol)
    print('Success! Try running the script again')
    


