class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            for ch in word:
                encoded.append(str(ord(ch)))
            encoded.append(str(ord(" ")))
        encoded.pop()
        return encoded

    def decode(self, s: str) -> List[str]:
        word= ""
        for ch in s:
            word += chr(int(ch))
        s = word.split(' ')
        return s
        
        

sol = Solution()
strs=["Hello","World"]

encoded = sol.encode(strs)
print(encoded)

decoded = sol.decode(encoded)
print(decoded)

        