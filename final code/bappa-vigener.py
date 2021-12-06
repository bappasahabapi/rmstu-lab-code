'''
author: bappa
github: bappasahabapi
'''


def Vigenere(text,s,Flag):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(Flag):
            result+=chr((ord(char)-97 +ord(s[i])-97)%26+ 97)
        else:
            result += chr((ord(char)- ord(s[i]) +26) % 26 + 97)
    return result
# assumption:- for simplicity i am only considering lowercase-values and without spaces
if __name__=="__main__":
    Plain=''.join(input("Enter PlainText: ").lower().split())
    Key=''.join(input("Enter Key: ").lower().split())
    s=''
    caterpillar=0
    for i in range(len(Plain)):
        s+=Key[caterpillar%len(Key)]
        caterpillar+=1
    CipherText=Vigenere(Plain,s,True)
    print("Vigener Cipher code:")
    print("Encrypted CipherText: ",CipherText)
    print("Decreyped CipherText: ",Vigenere(CipherText,s,False))
    print("Coded by bappa saha (2015-12-07)")


# Enter PlainText: bappa
# Enter Key: jixxi
# CipherText:  oiwwoxscwd
# Plainback: helloworld