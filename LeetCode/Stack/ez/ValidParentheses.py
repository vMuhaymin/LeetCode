class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = {'(', '{', '['}
        close = {')', '}', ']'}

        if not s:
            return True

        valid = []
        for i in s:
            if i in open:
                valid.append(i)
            else:
                j = valid.pop()
                if (i == '(' and j !=')' ) or (i == '{' and j !='}' ) or (i == '[' and j !=']' ):
                    return False
        return True

sol = Solution()
s ="([)]"
print(f"Output: {sol.isValid(s)}")