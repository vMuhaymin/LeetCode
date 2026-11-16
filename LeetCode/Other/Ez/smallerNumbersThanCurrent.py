class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for curr in range(len(nums)):
            l = 0 
            r = len(nums) - 1
            counter = 0
            while l < curr or r > curr :
                if l < curr :
                    if nums[curr] > nums[l]:
                        counter+=1
                    l+=1
                if r > curr :
                    if nums[curr] > nums[r]:
                        counter+=1
                    r-=1
            res.append(counter)
        return res


sol = Solution()
print(f" {sol.smallerNumbersThanCurrent(nums = [6, 5, 4, 8])} ")
