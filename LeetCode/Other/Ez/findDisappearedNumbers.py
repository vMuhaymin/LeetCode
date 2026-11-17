class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        nums = set(nums)
        counter = 1
        res = []
        for i in nums:
            if i == counter:
                counter+=1
                continue
            else:

                curr = i - 1
                while curr != counter:
                    res.append(counter)
                    counter+=1


        return res 


sol = Solution()
print(f" {sol.findDisappearedNumbers(nums = [1,1])} ")