class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        mid = int(r/2)
        print(f"mid is = {mid}")

        while l <= r :
            if target == nums[mid]:
                return mid
            elif target > nums[mid] :
                l = mid + 1
                mid = int((l + r)/2)
                
            else:
                r = mid - 1
                mid = int((l + r)/2)
            print(f"mid is = {mid}")
        return -1

sol = Solution()
res = sol.search([-1,0,3,5,9,12], 9)
print(f"Result is = {res}")