class Solution:

    def encode(self, strs) -> str:
        encoded =""
        for word in strs:
            for ch in word:
                encoded+= str(ord(ch))
                encoded += str('#')
            encoded += str('!')
            
        return encoded

    def decode(self, s: str):
        word= ""
        letter  = ""
        words = [] 

        for ch in s:
            if ch == "!":
                words.append(word)
                word = ""
            elif ch == "#":
                word += chr(int(letter))
                letter= ""
            else: 
                letter += ch

        return words

sol = Solution()
strs=["Muhaymin"]

encoded = sol.encode(strs)
print(f"The encoded is {encoded}")
print("-----------------------")

decoded = sol.decode(encoded)
print(f"The decoded is {decoded}")
print("-----------------------")

# class Solution:

#     def encode(self, strs) -> str:

#         counter = len (strs)
#         while counter > 0:
#             word = strs.pop(0)
#             if counter != 1 :
#                 word +=" "
#             for ch in word:
#                 strs.append(str(ord(ch)))
#             counter-=1


#     def decode(self, s: str):
#         word= ""
#         while s:
#             cara = s.pop(0)
#             word += chr(int(cara))  
#         words = word.split(' ')
#         for word in words:
#             s.append(word)

        
# sol = Solution()
# strs=["Hello","World"]

# encoded = sol.encode(strs)
# print(f"The encoded is {strs}")
# decoded = sol.decode(strs)
# print(f"The decoded is {strs}")
