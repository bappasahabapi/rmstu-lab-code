from random import randint

alphabets=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_text(plaintext):
    random_text=[]
    for rand in range(len(plaintext)):
        random_text.append(randint(0,len(alphabets)))
    return random_text

def encryption(plaintext,key):
    plaintext=plaintext.upper()
    ciphertext=""

    for sequence,text in enumerate (plaintext):
        key_sequence=key[sequence]
        text_sequence=alphabets.find(text)
        location=(key_sequence+text_sequence)
        ciphertext +=alphabets[(location)%len(alphabets)]
    return ciphertext

def decryption(cipher,key):
    cipher=cipher.upper()
    plaintext=""

    for sequence,text in enumerate (cipher):
        key_sequence=key[sequence]
        text_sequence=alphabets.find(text)
        new_location = (key_sequence - text_sequence)
        plaintext += alphabets[(new_location) % len(alphabets)]
    return plaintext

if __name__ == '__main__':
   plaintext = "coderbappa"
   key = random_text(plaintext)
   enc_text = encryption(plaintext, key)
   plaontext = decryption(enc_text, key)
   print("The encrypted message: ", enc_text)
   print("The decrypted message: ", plaintext)

