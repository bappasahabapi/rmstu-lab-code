import random

string = "abcdefghijklmnopqrstuvwxyz " 
n=len(string)

message = input("Enter the plain Text: ")
messLower = message.lower() 

def otp():
    key =""
    for i in range(len( message)):
        val=string[random.randint(0,n-1)] 
        key = key + val
    return key

key = otp() 
print("Genetated key: ", key)
keyLen=len(key)  

def encryption():
    cipher=""
    p=0                                     
    for i in messLower:
        position = string.find(i)          
        position2 =string.find(key[p])      
        newPosition = (position+position2)%n
        p=p+1
        p= p%keyLen
        cipher = cipher+ string[newPosition]
    return cipher

def decryption():
    plain=""
    p=0
    cipher = encryption()
    for i in cipher:
        position = string.find(i)
        position2= string.find(key[p])
        newPosition = (position-position2)%n
        p=p+1
        p=p%keyLen
        plain = plain+ string[newPosition]
    return plain

cipher=encryption()
plain =decryption()

print("The encrypted message of ",message,"is: ",encryption())
print("The decrypted message of is: ",decryption())

