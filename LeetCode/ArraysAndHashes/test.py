class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.strip(" ") == "" :
            return True

        s = s.lower()

        word= ""
        letters = {'a'}
        for letter in "qwertyuiopsdfghjklzxcvbnm":
            letters.add(letter)
        for ch in s:
            if ch in letters:
                word += ch
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
res = sol.isPalindrome("race a car")

print(f"The result is {res}")


    

    

     
