# this is coded by coder bappa/cse/session: 2015-2016

# ------------------RSA ALGORITHM STARTS------

from random import randint

MX = 400  # primes in (0 - MX)
number = [True for _ in range(MX + 1)]

i = 3
while i * i <= MX:
    if number[i]:
        j = i * i
        while j <= MX:
            number[j] = False
            j += i
    i += 2

primes = list()
primes.append(2)
i = 3
for i in range(3, MX, 2):
    if number[i]:
        primes.append(i)

# ------------- Generating RSA modulus 'n' -------------- #

p = primes[randint(0, len(primes)) - 1]
q = p
while q == p:
    q = primes[randint(0, len(primes) - 1)]
n = p * q
print("p =", p, "q =", q, "n =", n)

# ------------- Generating Public Key 'e' --------------- #

phi_of_n = (p - 1) * (q - 1)
# Second chose "Public key, e" such as
#   1 < e < phi(n) and gcd(e, phi(n)) = 1
from math import gcd

e = phi_of_n
while gcd(e, phi_of_n) != 1:
    e = randint(2, phi_of_n)
print("Public key (e, n) :", e, n)
print("This is RSA algorithm coded by coder bappa saha")

# ------------- Generating Private Key 'd' -------------- #

k = 0
d_float = 1.2
d = 1
while d != d_float:
    d_float = (1 + (k * phi_of_n)) / e
    d = int(d_float)
    k += 1
print("Private key (d, n) :", d, n)

# ------------- Taking Plain text as input -------------- #

plain = str(input("Give your input message: "))
print("\tYour input message is:", plain)

# ----------- Encrypting inputted plain text ------------ #
# Encryption formula : cipher = (plain)^e mod n
cipher = list()
for i in range(len(plain)):
    c = ord(plain[i])
    cipher.append(pow(c, e, n))
print("Encrypted message is:", cipher, "(in numerical form)")

# --------------- Decrypting cipher text ---------------- #
# Decryption formula : deciphered = (cipher)^d mod n
deciphered = str()
for i in range(len(cipher)):
    c = cipher[i]
    deciphered += chr(pow(c, d, n))
print("Decrypted message is:", deciphered)
