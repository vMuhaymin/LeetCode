class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """ Better sol : Time = O((n * log k) Space = # O(n + k) = O(n)

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

        # Sapce occur = {}   # O(n) worst case
        # heap = []    # O(k)
        # res = []     # O(k)

        """
        
        if len(nums) <= 1 or len(nums) == k:
            return nums
        
        nums.sort()

        #To calculate the frequency of the elements
        elementFrequency = {}

        for i in nums:
            if i in elementFrequency:
                elementFrequency[i] = elementFrequency.get(i) +1
            else:
                elementFrequency[i] = 1
        
        #Loop k times, every loop will drop the highest from elementFrequency, and add it to K_Frequencey k times
        K_Frequencey = []
        while k != 0 :
            highestFreq = 0
            for i in elementFrequency:
                if highestFreq < elementFrequency.get(i):
                    highestFreq = elementFrequency.get(i)
                    el = i 
            
            elementFrequency.pop(el)
            K_Frequencey.append(el)
            k -=1

        return K_Frequencey