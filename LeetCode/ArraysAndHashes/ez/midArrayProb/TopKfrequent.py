class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        elementFrequency = {}

        for i in nums:
            if i in elementFrequency:
                elementFrequency[i] = elementFrequency.get(i) +1
            else:
                elementFrequency[i] = 0
        
        K_Frequencey = []
        while k != 0 :
            highestFreq = 0
            for i in elementFrequency:
                if highestFreq < elementFrequency.get(i):
                    highestFreq = i
            K_Frequencey.append(highestFreq)
            k -=1


