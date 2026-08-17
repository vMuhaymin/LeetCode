class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        ## Better Solution, O(n)
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1 
                while y in nums:
                    y += 1
                best = max(best , y - x)
        return best
        """
        
        if not nums:
            return 0
        if len(nums)<= 1:
            return 1
        
        heapq.heapify(nums)
        root = heapq.heappop(nums)
        LC = {root}
        highest = 1
        while nums:
            
            secNum = heapq.heappop(nums)
            difference = abs(root - secNum)
            if (difference == 0 or difference == 1):
                if difference ==1:
                    LC.add(secNum)
                    if len(LC) > highest:
                        highest = len(LC)
                flag = False
            else:
                flag = True
                if flag:
                    LC = {root}
            root = secNum

            
        return highest