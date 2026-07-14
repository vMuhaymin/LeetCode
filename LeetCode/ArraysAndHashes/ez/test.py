class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        suffix= [1] * n
        prefix = [1] * n

        for i in range(n-2, -1 , -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        result = [prefix[i] * suffix[i] for i in range(n)]  
        print(result)

sol = Solution ()
sol.productExceptSelf([2, 3, 4, 5] )