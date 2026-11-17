class Solution:
    def findDisappearedNumbers(self, nums):
        res = []

        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
            print(f"f index = {index} | nums[index] = {nums[index]}")

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


sol = Solution()
print(f" {sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])} ")