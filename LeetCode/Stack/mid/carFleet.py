class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = []
        stack = []
        for i in range(len(speed)):
            pairs.append([position[i], speed[i]])

        pairs = sorted(pairs)[::-1]

        for d , t in pairs :
            
            time = float(target - d) / t
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

sol = Solution()
print(f"res = {sol.carFleet(12, [10,8,0,5,3] , [2,4,1,1,3])}") 