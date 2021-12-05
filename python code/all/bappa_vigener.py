alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vbappaencrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    cipher = ""
    key_index = 0

    for p in plain_text:
        index = (alphabets.find(p))
        new_index = (index + (alphabets.find(key[key_index]))) % len(alphabets)
        cipher = cipher + alphabets[new_index]
        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0
    return cipher

    # key1=key
    # cipher1=cipher
    # def vbappaendecrypt(ciphe1,key1):
    #     cipher=cipher.upper()
    #     key=key.upper()
    #     plaintext=""
    #     key_index=0

    # for d in cipher:
    #     index=(alphabets.find(d))
    #     new_index=(index-(alphabets.find(key[key_index])))%len(alphabets)
    #     plaintext=plaintext+alphabets[new_index]
    #     key_index=key_index+1
    #     if key_index == len(key):
    #        key_index=0
    # return plaintext


if __name__ == '__main__':
    plain_text = "hellowcoderbappa"
    print("Given Plaintext is: ", plain_text)
    enc_text = vbappaencrypt(plain_text, "secret")
    print("The encrypted message: ", enc_text)

#     cipher="zincspusfvvustrr"
#    dec_text= vbappaendecrypt(cipher,"secret")
#    print("The decrypted message: ",dec_text)
