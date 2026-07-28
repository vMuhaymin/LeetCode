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
        for letter in "qwertyuiopsdfghjklzxcvbnm1234567890":
            letters.add(letter)
        for ch in s:
            if ch in letters:
                word += ch
        if len(word) == 1:
            return True
        left = 0
        right = len(word) - 1 
        while left < right :
            if word[left] != word[right]:
                print(f"The letters are {word[left]} != {word[right]} ")
                return False
            left += 1
            right -=1
        return True


    




        
        

sol = Solution()
res = sol.isPalindrome("0a")

print(f"The result is {res}")


    

    

     
