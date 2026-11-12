class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rep = {}
        # unique = set(nums)
        # for i in unique :
        #     rep[i] = 0

        # for i in range(len(nums)):
        #     rep[nums[i]] = rep.get(nums[i]) + 1

        # for i in rep:
        #     if rep.get(i) == 1:
        #         return i

        #Solution using XOR
        result = 0 
        for n in nums:
            result ^= n # XOR will remove all duplicates  
        return result


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))