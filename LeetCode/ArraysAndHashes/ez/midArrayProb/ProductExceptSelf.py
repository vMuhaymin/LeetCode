class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix= [1] * n

        for i in range(n-2, -1 , -1):
            suffix = nums[i+1] * nums[i]
        print(suffix)


