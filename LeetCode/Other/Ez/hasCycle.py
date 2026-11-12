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

        # ** Bad solution **

        # if head is None or head.next is None:
        #     return False

        # node = head
        # while node.val != "":
        #     node.val = ""
        #     if node.next is not None:
        #         node = node.next
        #     else:
        #         return False 
        # return True

         # ** Better approach **
        
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False