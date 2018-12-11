import sys
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
import paths
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
sys.path.insert(0, '/home/pi/cipherSuite/paths.py')
import paths
sys.path.insert(0, 'C:\Users\KM\Desktop\cipherSuite\paths.py')
import paths
import cipherSuite
symPath = cipherSuite.path['symbols'] + 'valid.sym'
file = open(symPath)
SYMBOLS = file.read()
file.close()

def get(): return SYMBOLS
def add(symbol):
    file = open(symPath, 'a')
    file.write(symbol)
    file.close()
