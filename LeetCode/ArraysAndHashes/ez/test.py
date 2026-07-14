class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        suffix= [1] * n
        

        for i in range(n-2, -1 , -1):
            suffix[i] = nums[i+1] * suffix[i+1]
            print(f"Tha value of i = {i} and suffix of i is = {nums[i]}")
            
        
        print(suffix)

sol = Solution ()
sol.productExceptSelf([1,2,3,4])