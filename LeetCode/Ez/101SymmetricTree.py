# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, p):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # BFs
        stackT1 = []
        stackT2 = []

        #Check the root
        if p == None :
            return True
        elif (p.left != None and p.right == None) or (p.left == None and p.right != None):
            return False
        else:
            leftSubTree = p.left 
            rightSubTree = p.right 
        #Check the root of the sub trees
        if (leftSubTree.left != None and rightSubTree.left == None) or (leftSubTree.right == None and rightSubTree.right != None):
            return False

        stackT1.append(leftSubTree)
        stackT2.append(rightSubTree)

        while (stackT1) and (stackT2) :

            nodeT1 = stackT1.pop(0)
            nodeT2 = stackT2.pop(0)
            if nodeT1.val != nodeT2.val:
                return False
            
            if nodeT1.left != None and nodeT2.right != None:
                 stackT1.append(nodeT1.left)
                 stackT2.append(nodeT2.right)
            elif (nodeT1.left == None and nodeT2.right != None) or (nodeT1.right == None and nodeT2.left != None):
                return False

            if nodeT1.right != None and nodeT2.left != None:
                 stackT1.append(nodeT1.right)
                 stackT2.append(nodeT2.left)

            elif (nodeT1.right != None and nodeT2.left == None) or (nodeT1.left == None and nodeT2.right != None):
                return False

        if (stackT1 and not stackT2) or (not stackT1 and stackT2):
            return False 
        return True