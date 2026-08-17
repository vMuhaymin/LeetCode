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
            else:
                if valid:
                    j = valid.pop()
                    print(f" i= {i} | j = {j}" )
                    if (i == '(' and j ==')' ) or (i == '{' and j =='}' ) or (i == '[' and j ==']' ):
                        continue
                    else:
                        return False
                else:
                    return False
        return True

sol = Solution()
s ="([])"
print(f"Output: {sol.isValid(s)}")