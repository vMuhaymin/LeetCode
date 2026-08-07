class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = ""
        chars = []
        for ch in s:
            if ch.isalnum():
                #tmp+= ch  makes it O(n), in Total O(n^2) !
                chars.append(ch.lower())
        #tmp = tmp.lower()
        tmp  = tmp.join(chars)
        
        left = 0
        right = len(tmp) - 1 
        while left < right :
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -=1
        return True