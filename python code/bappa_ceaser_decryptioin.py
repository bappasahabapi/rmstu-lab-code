message = input('enter your decrypted message: ')
# here I enter my encrypted message htijwgfuuf
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = int(input('enter your key:'))
# key =5
decrypt = ''
for i in message:
    position = alphabet.find(i)
    newposition = position - key
    decrypt += alphabet[newposition]
print('decrypted message is : ' + decrypt)
# the plain text after decryption is -->  coderbappa