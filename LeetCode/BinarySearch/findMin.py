class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, r = 0 , len(nums) - 1
        mid = (l + r)// 2

        while l < r :

            if nums[l] < nums[mid] and nums[l] < nums[r] :
                r = mid - 1
                mid = (l + r) // 2
            elif nums[r] < nums[mid] and nums[r] < nums[l] :
                l = mid + 1
                mid = (l + r) // 2
            elif nums[l] <  nums[r] :
                l = mid
                mid = (l+ 1 + r) // 2
            else:
                r = mid
                mid = (l+ r - 1) // 2 

        return nums[mid]

sol  = Solution()
