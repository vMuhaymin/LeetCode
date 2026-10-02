class Solution(object):
    def dailyTemperatures(self, temperatures):

        """
        :type temperatures: List[int]
        :rtype: List[int]
        """     
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp :
                curr = stack.pop()
                res[curr] = i - curr 
            stack.append(i)

        return res
