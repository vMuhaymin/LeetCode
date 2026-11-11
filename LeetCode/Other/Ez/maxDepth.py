# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        counter = 1
        stack.append([root , counter])
        max_depth = 0

        while stack :

            info = stack.pop()
            node , depth = info[0] , info[1]

            if depth > max_depth:
                max_depth = depth
            if node is not None:
                if node.left is not None :
                    stack.append([node.left , depth + 1])
                if node.right is not None : 
                    stack.append([node.right , depth + 1])
            
            