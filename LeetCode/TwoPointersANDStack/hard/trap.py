class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        Optimal Solution:
        #####################        
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
        ##################### 
        
        """

        i = 0 
        count = 0
        while i < len(height) - 1:
            while height[i] == 0:
                i+=1
                continue
            j = i + 1
            total = 0
            while height[i] > height[j] and j < len(height) - 1:
                total = total + height[i] - height[j]
                print(f"The formula is  height[i] = {height[i]} - height[j]= {height[j]} ")
                j+=1

          
            count = count + total
            print(f"The total = {total}, count = {count} ")
            i = j 
        return count




sol = Solution()

print(f"Output: {sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])}")
