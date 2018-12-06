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
