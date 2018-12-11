import paths
import sys, os

path = {}
file = open('paths')
paths = file.read()
for line in paths.split('\n'):
    if line[0] != '#': # Allows for commenting ;)
        word = line.split()
        cwd = os.path.dirname(os.path.abspath(__file__))
        fullPath = str(cwd) + word[1]
        path[word[0]] = fullPath
        sys.path.insert(0, fullPath)

# os.listdir()
def writePathsToPy():
    for folder in path:
        folderContents = os.listdir(path[folder])
        if not 'external' in folder:
            for item in folderContents:
                if '.py' in item and folder != 'cipherSuite':
                    pyPath = path[folder]+item
                    file = open(pyPath)
                    pyContents = file.read()
                    file.close()

                    importSys = 'import sys\n'
                    insertDir = "sys.path.insert(0, r'%s')\n" % (os.path.abspath(__file__))
                    importPaths = 'import paths\n'
                    
                    if not importPaths in pyContents:
                        pyContents = importPaths + pyContents
                    if not insertDir in pyContents:
                        if not 'sys.path.insert(0, ' in pyContents:
                            pyContents = insertDir + pyContents
                        else:
                            splitContents = pyContents.split('\n')
                            pyContents = ''
                            for line in range(len(splitContents)):
                                if 'sys.path.insert(0, ' in splitContents[line]:
                                    splitContents[line] = insertDir[:-1]
                                pyContents += splitContents[line] + '\n'
                    if not importSys in pyContents:
                        pyContents = importSys + pyContents

                    file = open(pyPath, 'w')
                    file.write(pyContents)
                    file.close()

def test():
    writePathsToPy()

def testHello():print('hello')

if __name__ == '__main__':
    test()
