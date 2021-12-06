# for encryption , e= (p+k)mod 26
# for decryption , d= (p-k)mod 26

string = "abcdefghijklmnopqrstuvwxyz " 
# Length=len(string)

message = input("Enter the plain Text: ")
messLower=message.lower()
key = int(input("Enter the key for encryption & decryption: "))


def encryption():
    cipher=""
    for i in messLower:
        position = string.find(i)
        newPosition = (position+key)%26
        cipher = cipher+ string[newPosition]
    return cipher
print("The encrypted message of ",message,"is: ",encryption())

def decryption():
    plain=""
    cipher = encryption()
    for i in cipher:
        position = string.find(i)
        newPosition = (position-key)%26
        plain = plain+ string[newPosition]
    return plain
print("The decrypted message of is: ",decryption())

