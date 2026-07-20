class Solution:

    def encode(self, strs) -> str:
        encoded = []
        for word in strs:
            for ch in word:
                encoded.append(str(ord(ch)))
            encoded.append(str(ord(" ")))
        encoded.pop()
        
        return encoded

    def decode(self, s: str):
        word= ""
        for ch in s:
            word += chr(int(ch))
        s = word.split(' ')
        return s
        
        

sol = Solution()
strs=["Hello","World"]

encoded = sol.encode(strs)
print(f"The encoded is {encoded}")

decoded = sol.decode(encoded)
print(f"The decoded is {decoded}")


class Solution:

    def encode(self, strs) -> str:

        counter = len (strs)
        while counter > 0:
            word = strs.pop(0)
            if counter != 1 :
                word +=" "
            for ch in word:
                strs.append(str(ord(ch)))
            counter-=1
        return strs

    def decode(self, s: str):
        word= ""
        while s:
            cara = s.pop(0)
            word += chr(int(cara))  
        words = word.split(' ')
        for word in words:
            s.append(word)
        return  s
        
sol = Solution()
strs=["Hello","World"]

encoded = sol.encode(strs)
print(f"The encoded is {encoded}")
decoded = sol.decode(encoded)
print(f"The decoded is {decoded}")
