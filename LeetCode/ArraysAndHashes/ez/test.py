import heapq
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
                    print(f'the two num are {root} and { secNum}')
                    LC.add(secNum)
                    if len(LC) > highest:
                        highest = len(LC)
                    print(LC)
                flag = False
            else:
                flag = True
                print(f"The nums are {secNum} and {root} flag is = {flag}")
                if flag:
                    LC = {root}
            root = secNum
            # if nums:
            #     root = heapq.heappop(nums)
            #     if flag:
            #         LC = {root}
            #     else:
            #         LC.add(root)
            #     if not nums:
            #         difference = abs(root - secNum)
            #         if ( difference == 0 or difference == 1):
            #             print(f'the two num are {root} and { secNum}')
            #             if difference ==1:
            #                 LC.add(secNum)
            #                 if len(LC) > highest:
            #                     highest = len(LC)
            #                 print(LC)
            
        return highest


sol = Solution()
nums = [100,4,200,1,3,2]
print(f"The num of consec is {sol.longestConsecutive(nums)}")

                
            




        