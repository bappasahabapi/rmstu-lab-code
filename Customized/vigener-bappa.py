# for encryption , e= (p+k)mod 26
# for decryption , d= (e-k)mod 26
# here the key must equal to the plaintext
# if the key is small then i repeated the key as long as it is equal to the plain text .
#messege=givemoney , key=lock

string = "abcdefghijklmnopqrstuvwxyz " 
# Length=len(string)

message = input("Enter the plain Text: ")
messLower=message.lower()
key = (input("Enter the key for encryption & decryption: "))  # key is a word here.
keyLen=len(key)   # take the key length


def encryption():
    cipher=""
    p=0                                      ## key er p namok postiion 
    for i in messLower:
        position = string.find(i)          ## position for plain text's character
        position2 =string.find(key[p])      ## position for key character## kehane ami key er p namok position ta find korbo.
        newPosition = (position+position2)%26
        p=p+1
        p= p%keyLen
        cipher = cipher+ string[newPosition]
    return cipher
print("The encrypted message of ",message,"is: ",encryption())

def decryption():
    plain=""
    p=0
    cipher = encryption()
    for i in cipher:
        position = string.find(i)
        position2= string.find(key[p])
        newPosition = (position-position2)%26
        p=p+1
        p=p%keyLen
        plain = plain+ string[newPosition]
    return plain
print("The decrypted message of is: ",decryption())

