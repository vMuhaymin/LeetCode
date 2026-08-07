class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s)!=len(t):
            return False

        for x in set(s):
            print(f's.count(x) is {s.count(x)} and t.count(x) is {t.count(x)}')
            if s.count(x) != t.count(x):
                print(f"s = {s} and t = {t}")
                return False
        return True

sol = Solution()
print(f"The result is {sol.isAnagram("rat","car")}")
                       
        