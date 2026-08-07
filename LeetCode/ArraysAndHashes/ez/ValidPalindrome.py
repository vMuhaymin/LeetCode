class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #Time: O(n), Space: O(n)
        tmp = ""
        for ch in s:
            if ch.isalnum():
                tmp+= ch

        tmp = tmp.lower()
        
        left = 0
        right = len(tmp) - 1 
        while left < right :
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -=1
        return True