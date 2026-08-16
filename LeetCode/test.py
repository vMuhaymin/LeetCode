class Solution:
    def trap(self, height):

        start = 0
        end = len(height) - 1

        maxLeft = 0
        maxRight = 0
        totalWater = 0

        while start < end :
            maxLeft = max(maxLeft, height[start])
            maxRight = max(maxRight, height[end])

            if maxLeft < maxRight :
                totalWater += maxLeft - height[start]
                start += 1
            else:
                totalWater += maxRight - height[end]
                end -=1
        return totalWater