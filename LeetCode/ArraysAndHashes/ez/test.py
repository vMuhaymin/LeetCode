word = "Hello Word"
encoded = []

for ch in word:
    encoded.append(str(ord(ch)))


decoded = []


word = ''
for ch in encoded:
    print(chr(int(ch)))
    word +=(chr(int(ch)))
print(word)
print(word.split(" "))
