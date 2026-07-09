class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        if len(nums) <= 1:
            return False
        
        for i in range(nums-1):
            if nums[i] == nums[i+1]:
                return True
        if nums[len(nums)-1] == nums[len(nums)-2]:
            return True
        return False
                       
        