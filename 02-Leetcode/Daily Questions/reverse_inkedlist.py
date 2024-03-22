
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head.next
        prev_node =  head

        if head is null or head.next is null:
            return 0

        while current_node != null: # last node
            next_node = current_node.next
            current_node.next = prev_node 

            # update
            prev_node = current_node
            current_node = next_node

        head.next = null
        head = prev_node











        