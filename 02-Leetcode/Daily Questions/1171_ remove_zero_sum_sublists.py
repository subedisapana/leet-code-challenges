"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Approach:

1.In case of linked list, you need to traverse the node one by one summing their values.
2. Since its a linked list, there will be head value indicating the first node.

1-> 4 -> 3 -> -3 -> 5

here, 1+4 gives 5, and on addding 5 with 3 gives 8, sequentially, on addition of -3 gives 5 back
we can see, there was summed value 5 on adding 2 nodes gives 5 again, so there should be sth equal to 0.

prefix_sum = sum one node after another: initially prefix sum = 0, if prefix sum repeats, then you will get ideas about which node to remove? you will not even enter in the map table

3. Initially, when prefix_sum = 0; we need to create a head for this prefix sum. so lets call that dummy node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):

        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next
