class Solution:

    def encode(self, strs: List[str]) -> str:
        counter = len (strs)
        while counter > 0:
            word = strs.pop(0)
            if counter != 1 :
                word +=" "
            for ch in word:
                strs.append(str(ord(ch)))
            counter-=1
        return strs 

    def decode(self, s: str) -> List[str]:
        word= ""
        while s:
            cara = s.pop(0)
            word += chr(int(cara))  
        words = word.split(' ')
        for word in words:
            s.append(word)
        return s 
        
