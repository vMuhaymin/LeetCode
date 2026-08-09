class Solution(object):
    def productExceptSelf(self, nums):

        p = [1] * len(nums)
        s = [1] * len(nums)


        p = 1
        for i in range(1, len(nums) - 1):
            p = p[i - 1 ] * nums[i - 1]
        for i in range(len(nums)-2 , -1, -1):
            s[i] = s[i+1] * nums[i+1]
        return [s[i] * p[i] for i in range(len(nums))]

sol = Solution()
print(f"The result is {sol.productExceptSelf([1,2,3,4])}")
