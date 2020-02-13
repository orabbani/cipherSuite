message = input('message: ')
key = int(input('key: '))
translation = ''

for c in message:
    translation += chr(ord(c) + key)
    
print(translation)