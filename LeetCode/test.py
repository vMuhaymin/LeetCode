class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 1 and nums[i-1] == nums[i]:
                pass
            j= i + 1
            k = len(nums)-1

            while j < k :
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    res.append([nums[i],  nums[j] , nums[k]])
                    j=j+1
                    while nums[j-1] == nums[j] and j < k:
                        j=j+1
        return res

sol = Solution()
print(f"The result is : {sol.threeSum([-100,-70,-60,110,120,130,160])}")

