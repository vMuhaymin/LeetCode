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
            if height[i + 1] > height[j-1]:
                i+=1
            elif height[i + 1] < height[j-1]:
                j-=1
            else:
                print(f"The heights are i[{i}] = {height[i]} j[{j}]= {height[j]}")
                if height[i] > height[j]:
                    print(f" j is chosen")
                    j-=1
                else:
                    i+=1
                    print(f" i is chosen")
        return area

sol = Solution()
print(f"The max height = {sol.maxArea([1,2,4,3])}")
