class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums_set = set(nums)
        # res = []
        # for i in range(1 , len(nums)+1):
        #     if i not in nums_set:
        #         res.append(i)
        # return res 

        ## Optimal 
        res = []
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index]) 
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
                
    
