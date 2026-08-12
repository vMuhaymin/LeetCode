class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,len(nums)-1):
            L = 0
            while L < i :
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[L] + nums[j] == 0 :
                        if [nums[L] ,nums[i] , nums[j]] not in res:
                            res.append([nums[L] ,nums[i] , nums[j]])
                L+=1                        
        return res

sol = Solution()
print(f"The result is : {sol.threeSum([0,1,1])}")

