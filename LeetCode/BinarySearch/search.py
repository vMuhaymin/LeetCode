class Solution(object):
    def search(self, nums, target):

        l, r = 0 , len(nums) - 1
        mid = (l + r)// 2

        while l <= r :
            if nums[mid] == target:
                return mid
            
            #Check left sub array
            elif nums[l] <= nums[mid] :
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else :
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 
            mid = (l + r)// 2
            
        return - 1 
                    

        