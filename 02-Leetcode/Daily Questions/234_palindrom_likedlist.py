"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l]!= nums[r]:
                return False
            l+=1
            r-=1
        return True

"""  
How can we do it in a 0(1) of memory? By using fast and slow pointer
But, why? Slow ptr moves 1 spot ahead and fast moves 2 spot ahead
We could check the beginning and the end and then i+1 and j-1, but since its a singly linked list, it only moves in a direction
There's a algorithm to reverse the linkedlist
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next: # keep going until fast is at the last node or null
            fast = fast.next
            fast = fast.next
            slow = slow.next # only one step ahead

        #reverse 2nd half 
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True