class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        
        if len(nums) != len(set(nums)):
            return True

        return False


sol = Solution()
print(f"The result is {sol.hasDuplicate([1,3,4,2])}")
                       
        