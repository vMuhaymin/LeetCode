class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l= 0
        r = len(nums) - 1
        if r == 0:
            if target == nums[0]:
                return 0
        mid = int(r/2)
        while l <= r :
            if target == nums[mid]:
                return mid
            elif target > nums[mid] :
                l = mid + 1
                mid = int((mid + r)/2)
            else:
                r = mid - 1
                mid = int((mid + r)/2)
        return -1

