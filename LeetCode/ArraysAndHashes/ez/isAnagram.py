class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
            O(n²)
        if len(s) != len(t):
            return False
        for ch in s:
            if s.count(ch) != t.count(ch):
                return false
        return True

        """ 
        #########################################
        """
            Dynamic Programming O(n) and Space O(n)
        """

        if len(s) != len(t):
            return False
        
        freqS = {}
        freqT = {}

        for i in s :
            if i in freqS:
                freqS[i] = freqS.get(i) + 1
            else:
                freqS[i] = 0

        for i in t :
            if i in freqT:
                freqT[i] = freqT.get(i) + 1
            else:
                freqT[i] = 0
        
        if len(freqT) != len(freqS):
            return False

        else:
            for i in freqS:
                if i not in freqT:
                    return False
                else: 
                    if freqT[i] != freqS[i]:
                        return False
        return True

