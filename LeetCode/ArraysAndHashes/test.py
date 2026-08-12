class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,len(nums)-1):
            L , R  = 0 , len(nums) - 1
            while L < i and i < R :
                if nums[i] + nums[L] + nums[R] == 0 :
                    print(f"FOUND ! {[nums[L] ,nums[i] , nums[R]]}")
                    res.append([nums[L] ,nums[i] , nums[R]])
                if L < i and R > i :
                    L+=1
                    R-=1
                elif L < i and R - 1 == i :
                    L+=1
                elif R > i and L + 1 == i:
                    R-=1
                else :
                    L+=1 # Flag to stop
        return res

sol = Solution()
print(f"The result is : {sol.threeSum([-1,0,1,2,-1,-4])}")

