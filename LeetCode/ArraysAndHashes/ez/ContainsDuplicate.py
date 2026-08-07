class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #len func is O(1)
        #set(nums) O(n)
        if len(nums) != len(set(nums)):
            return True

        return False
        