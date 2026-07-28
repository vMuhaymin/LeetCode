class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """



        if s.strip(" ") == "" or len(s) == 1:
            return True
        s = s.lower()

        word= ""
        letters = {'a'}

        #Removing all non-alphanumeric characters
        for letter in "qwertyuiopsdfghjklzxcvbnm1234567890":
            letters.add(letter)
        for ch in s:
            if ch in letters:
                word += ch

        if len(word) == 1:
            return True

        #2 Pointers
        left = 0
        right = len(word) - 1 
        while left < right :
            if word[left] != word[right]:
                return False
            left += 1
            right -=1
        return True