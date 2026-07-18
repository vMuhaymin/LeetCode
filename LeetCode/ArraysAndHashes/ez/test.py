word = "Hello Word"

ls = []
for ch in word:
    ls.append(ord(ch))
print(ls)
la =[]
word = ""
for ch in ls:
    if ch == 32:
        la.append(word)
        word = ""
    else:
        word+= chr(ch)

print(la)