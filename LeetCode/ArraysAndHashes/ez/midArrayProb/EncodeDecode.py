class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            for ch in word:
                encoded.append(ord(ch))

    def decode(self, s: str) -> List[str]:
        decoded = []
        word= ""
        for i in range(len(s)):
            if s[i] == 32 or i == len(s) -1:
                
                if i == len(s) -1 :
                    word += chr(s[i])
                    decoded.append(word)
                else:
                    decoded.append(word)
                
                word = ""
            else:
                word += chr(s[i])