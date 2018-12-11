sys.path.insert(0, 'C:\Users\KM\Desktop\cipherSuite\paths.py')
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
                if '.py' in item:
                    pyPath = path[folder]+item
                    file = open(pyPath)
                    pyContents = file.read()
                    file.close()
                    string =  "sys.path.insert(0, '%s')\n" % (os.path.abspath(__file__))
                    string += 'import paths\n'
                    string += pyContents
                    print(string)
                    file = open(pyPath, 'w')
                    file.write(string)
                    file.close()

                    

                   
                            
                
               
def test():
    writePathsToPy()

def testHello():print('hello')

if __name__ == '__main__':
    test()
