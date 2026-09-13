class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def treeGen(left, right , curr):
            if len(curr) == 2 * n :
                res.append(curr)
            if left < n:
                treeGen(left + 1 , right, curr+'(')
            if right < left :
                treeGen(left, right+1 , curr+')')
        treeGen(0,0,'')
        return res 




        

        