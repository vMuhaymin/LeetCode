class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):        
            comp = target - num
            if comp in seen:
                return[ seen[comp], i ]
            seen[num]= i


Sol = Solution()
nums = [11,2, 7,15]
target = 9
print("------------------------------------------")
print(f" The two sums in {Sol.twoSum(nums, target)} ")