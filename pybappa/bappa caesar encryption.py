message= input('enter your  message: ')
# here I enter the message coderbappa
alphabet='abcdefghijklmnopqrstuvwxyz '
key=int(input('enter your key:'))
# key =5
encrypt=''
for i in message:
    position=alphabet.find(i)
    newposition=position+key
    encrypt+=alphabet[newposition]
print('encrypted message is : '+encrypt)
# the final output of coderbappa is -->  htijwgfuuf
