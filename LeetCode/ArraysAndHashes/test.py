import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1
            
        heap = []
        for key in occur:
            heapq.heappush(heap, (occur[key], key)) # One item is O(logn), whole items (nlogn)
            if len(heap) > k :
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]


sol = Solution()
print(f"Output: {sol.topKFrequent([1,1,1,2,2,3], k = 2)}")