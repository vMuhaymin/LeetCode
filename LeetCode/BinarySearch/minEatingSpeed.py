from math import * 
class Solution:
    def minEatingSpeed(self, piles, h):

        low = 1
        high =  max(piles)

        while low <= high:
            k = (low+high)//2
            hours = sum(math.ceil(pile/k) for pile in piles)

            if hours <= h:
                low = k - 1
            else:
                high = k + 1

        return low 


