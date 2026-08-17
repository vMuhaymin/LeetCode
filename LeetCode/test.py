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
                print(f'{i} is appended')
            elif i in close and valid:
                j = valid.pop()
                print(f" i= {i} | j = {j}" )
                if (j == '(' and i ==')' ) or (j == '{' and i =='}' ) or (j == '[' and i ==']' ):
                    continue
                else:
                    return False
            else:
                return False
        return True

sol = Solution()
s ="()"
print(f"Output: {sol.isValid(s)}")