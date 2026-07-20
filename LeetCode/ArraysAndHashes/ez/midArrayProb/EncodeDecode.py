class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =""
        for word in strs:
            for ch in word:
                encoded+= str(ord(ch))
                encoded += str('#')
            encoded += str('!')
            
        return encoded

    def decode(self, s: str) -> List[str]:
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
        
