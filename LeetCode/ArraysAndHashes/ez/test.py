class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
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