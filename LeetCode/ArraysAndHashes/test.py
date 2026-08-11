class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(numbers) == 2 :
            return [1,2]
        i = 0
        j = len(numbers) - 1
        while i <= j :
            if numbers[i] + numbers[j] == target:
                return [i+1 , j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i += 1
sol = Solution()

print(f"Output : {sol.twoSum([-1000,-1,0,1], target = 1)}")