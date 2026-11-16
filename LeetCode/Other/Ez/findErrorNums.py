class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums= sorted(nums)
        nonDupList = set(nums)

        missed = 1
        for i in nonDupList:
            if missed in nonDupList:
                missed +=1
                continue
            else:
                break
        j=0
        for i in nonDupList:
            if nums[j] == i:
                j+=1
                continue
            else:
                return [nums[j] , missed]
        return [nums[j] , missed]

sol = Solution()
print(f" {sol.findErrorNums(nums = [1, 1])} ")