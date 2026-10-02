class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        fleet = {}
        for i in range(len(position)):
            addition = position[i] + speed[i]
            if addition in fleet and target >= addition:
                fleet[addition]= fleet.get(addition) + 1
            elif target >= addition:
                fleet[addition] = 0

        print(fleet)

        return len(fleet)


sol = Solution()
print(f"res = {sol.carFleet(100, [0,2,4] , [4,2,1])}") 