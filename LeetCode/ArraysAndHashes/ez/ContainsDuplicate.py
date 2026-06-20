class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        seen = {}
        for i, num in enumerate(length):
            seen[num] = i


        return False
                       
        