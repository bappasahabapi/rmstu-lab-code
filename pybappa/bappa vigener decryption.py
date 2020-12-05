alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vbappaendecrypt(cipher,key):
    cipher=cipher.upper()
    key=key.upper()
    plaintext=""
    key_index=0

    for d in cipher:
        index=(alphabets.find(d))
        new_index=(index-(alphabets.find(key[key_index])))%len(alphabets)
        plaintext=plaintext+alphabets[new_index]
        key_index=key_index+1
        if key_index == len(key):
           key_index=0
    return plaintext


if __name__ == '__main__':
   cipher="zincspusfvvustrr"
   dec_text=vbappaendecrypt(cipher,"secret")
   print("The decrypted message: ",dec_text)
