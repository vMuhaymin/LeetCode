class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            for ch in word:
                encoded.append(str(ord(ch)))

    def decode(self, s: str) -> List[str]:
        word= ""
        for ch in s:
            word += chr(int(ch))
        s = [word]
        return s.split(' ')
        
