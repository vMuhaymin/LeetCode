class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i , j = 0 , len(height) - 1
        count = 0
        tempCount = 0

        while i < len(height) - 2:
            if height[i] == 0:
                i+=1
                continue
            j = len(height) - 1
            # minHeight = min(height[i] , height[j])
            # tempCount = minHeight * (j - i)

            minHeight = min(height[i] , height[j])
            tempCount =  minHeight * (j - i - 1)
            started_j = j 
            while  i < j - 1 :
                j -= 1
                if height[j] > height[i]:
                    minHeight = min(height[i] , height[j])
                    tempCount =  minHeight * (j - i - 1)
                elif height[started_j] < height[j] and height[i] >= height[j]:
                    started_j = j 
                    minHeight = min(height[i] , height[j])
                    tempCount =  minHeight * (j - i - 1)
                else:
                    tempCount = tempCount - height[j]
            
            print(f"The tempCount = {tempCount} and count = {count}")
            count = count + tempCount
            i = j

        return count


sol = Solution()

print(f"Output: {sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])}")