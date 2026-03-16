# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #temp refrences 

        #Check the root
        if p.val != q.val:
            return False
        tempP = p.left
        tempQ = q.left

        #Checking the leftSide  
        while  tempP.left != None and tempQ.left != None :
            if tempP.val != tempQ.val:
                return False
            tempP = tempP.left
            tempQ = tempQ.left
            if (tempP.left != None and tempQ.left == None) or (tempP.left == None and tempQ.left != None):
                return False 
        
        tempP = p.right
        tempQ = q.right

        #Checking the right
        while  tempP.right != None and tempQ.right != None :
            if tempP.val != tempQ.val:
                return False
            tempP = tempP.right
            tempQ = tempQ.right
            if (tempP.right != None and tempQ.right == None) or (tempP.right == None and tempQ.right != None):
                return False
        return True   
            
