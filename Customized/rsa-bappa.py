num=[1 for i in range (0,200)]
p=2
num[0]=0
num[1]=0
while(p<=200):
    i=2
    while(p*i<200):
        if num[p*i]==1:
            num[p*i]=0
        i+=1
    p+=1
primes=list()
for i in range (0,200):
    if num[i]==1:
        primes.append(i)


import random
from math import gcd
# ------------- Generating RSA modulus 'n' -------------- 
p=primes[random.randint(0,len(primes))]
q=p
while p==q :
    q=primes[random.randint(0,len(primes))]
n=p*q
phi=(p-1)*(q-1)

print("p =",p,"q =",q,"n =",n)

# ------------- Generating Public Key 'e' --------------- 

pubkey=phi  #1<pubkey<phi(n)

while gcd(pubkey,phi)!= 1:
    pubkey=random.randint(2,phi-1)
print("Public key : ",pubkey)

d=(phi+1)/pubkey #d=((phi(n)*i)+1)/e
i=2
while(d!=int(d)):
    d=((phi*i)+1)/pubkey
    i+=1

privkey=int(d)
print("Private key : ",privkey)




msg=input("Enter the plain text : ")
#Encryption  c=p^e mod n
c = list()
for i in range(len(msg)):
    val = ord(msg[i])
    c.append(pow(val, pubkey, n))
print("Encrypted text = ", c)

#Decryption  p=c^d mod
decrypt = ""
for i in range(len(c)):
    val = c[i]
    decrypt+= chr(pow(val, privkey, n))
print("Decrypted text:", decrypt)