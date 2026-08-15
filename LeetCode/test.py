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

            minHeight = min(height[i] , height[j])
            tempCount =  minHeight * (j - i - 1)
            started_j = j 
            while  i < j - 1 :
                j -= 1
                if height[j] >= height[i]:
                    minHeight = min(height[i] , height[j])
                    tempCount =  minHeight * (j - i - 1)
                    started_j = j
                elif height[started_j] <= height[j]:
                    started_j = j 
                    minHeight = min(height[i] , height[j])
                    tempCount =  minHeight * (j - i - 1)
                else:
                    tempCount = tempCount - height[j]
                    print(f"i = {i} and k = {j}")
            count = count + tempCount
            print(f"The tempCount = {tempCount} and count = {count}")
            i = started_j
        return count


sol = Solution()

print(f"Output: {sol.trap( [4,2,0,3,2,5])}")