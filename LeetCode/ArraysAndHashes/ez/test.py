word = "Hello Word"
encoded = []

for ch in word:
    encoded.append(ord(ch))


decoded = []
meow = ["ss" , 'Ssdas ']
word = ""
for i in range(len(encoded)):
    if encoded[i] == 32 or i == len(encoded) -1:
        
        if i == len(encoded) -1 :
            word += chr(encoded[i])
            decoded.append(word)
        else:
            decoded.append(word)
        
        word = ""
    else:
        word += chr(encoded[i])

meow = decoded

print(meow)
