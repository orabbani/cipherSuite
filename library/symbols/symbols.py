import sys
sys.path.insert(0, r'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
symPath = paths.path['symbols'] + 'valid.sym'
file = open(symPath)
SYMBOLS = file.read()
file.close()

def get(): return SYMBOLS
def add(symbol):
    file = open(symPath, 'a')
    file.write(symbol)
    file.close()

