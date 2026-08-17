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

        res = []
        for i in s:
            if i in open:
                res.append(i)
                print(f'{i} is appended')
            elif i in close and res:
                j = res.pop()
                print(f" i= {i} | j = {j}" )
                if (j == '(' and i ==')' ) or (j == '{' and i =='}' ) or (j == '[' and i ==']' ):
                    continue
                else:
                    return False
            else:
                return False

        return len(res) == 0