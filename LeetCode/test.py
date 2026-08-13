class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1:
            return 1

        i , j = 0, len(height) - 1
        area = min(height[i],height[j]) * (j - i)
        while i < j:
            area = max(area, (min(height[i],height[j]) * (j - i)) )
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return area

sol = Solution()
print(f"The max height = {sol.maxArea([1,8,6,2,5,4,8,3,7])}")
