# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next is None:
            return False

        node = head
        unique = set()
        while node.val not in unique:
            unique.add(node.val)
            if node.next is not None:
                node = node.next
            else:
                return False
        return True
        
