import heapq
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<= 1:
            return 0
        
        heapq.heapify(nums)
        root = heapq.heappop(nums)
        LC = []
        highest = 1
        while nums:
            LC.append(root)
            secNum = heapq.heappop(nums)
            difference = abs(root - secNum)
            if ( difference == 0 or difference == 1):
                if difference ==1:
                    LC.append(secNum)
                    if len(LC) > highest:
                        highest = len(LC)
                    print(LC)
            else:
                LC = []
            if nums:
                root = heapq.heappop(nums)
        return highest


sol = Solution()
nums =[1,1 , 2]
print(f"The num of consec is {sol.longestConsecutive(nums)}")

                
            




        