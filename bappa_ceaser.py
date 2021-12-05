# here I enter the message coderbappa
message = input('enter your  message: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = int(input('enter your key:'))
# key =5
encrypt = ''
for i in message:
    position = alphabet.find(i)
    newposition = position + key
    encrypt += alphabet[newposition]
print('encrypted message is : ' + encrypt)
# the final output of coderbappa is -->  htijwgfuuf

# ------ decryption part
# here I enter my encrypted message htijwgfuuf
# message = input('enter your decrypted message: ')
message = encrypt
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key1 = key

decrypt = ''
for i in message:
    position = alphabet.find(i)
    newposition = position - key1
    decrypt += alphabet[newposition]
print('decrypted message is : ' + decrypt)
# the plain text after decryption is -->  coderbappa