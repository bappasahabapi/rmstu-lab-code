message="xsyza"
alphabets="abcdefghijklmnopqrstuvwxyz"

for key in range (len(alphabets)):
      plaintext=""
      for i in message:
            if i in alphabets:
                location=alphabets.find(i)
                location=location-key
                if location<0:
                     location=location + len(alphabets)
                plaintext=plaintext + alphabets[location]
            else:
                plaintext=plaintext+i
      print("key #%s: #%s" %(key,plaintext))
