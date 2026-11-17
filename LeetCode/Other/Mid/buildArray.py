class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        j = 0
        res= []
        for i in range(1 , n+1):
            if j < len(target):
                res.append("Push")
                if i == target[j]:
                    j+=1
                elif res:
                    res.append('Pop')
            else:
                break
        return res


sol = Solution()
print(f" {sol.buildArray(target = [1,2], n = 4)} ")
