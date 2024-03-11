"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


1. Given the arrays of nums1 and nums2, we have to sort in ascending order merging both nums1 and nums2.
2. It has given that nums1 stores merged array as it has space to accommodate both.

Ways:
1.We have enough empty space at the last of nums1 and sorting gets easier when we compare and merge integers from end.
2.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1  # Pointer for the end of nums1
        p2 = n - 1  # Pointer for the end of nums2
        p = m + n - 1  # Pointer for the end of the merged list

        while m>0 and n>0: # while there's elements
            if nums1[p1] > nums2[p2]: # checks last index elements
                nums1[p] = nums1[p1]
                m-=1 # update pointer
            else:
                nums1[p] = nums2[p2] # if nums2 element greater
                n-=1
            p -=1 # regardless of what element we insert, we decrement the index

        # when there is element smaller than nums2, we put the remaining to the begining of the nums1

        while n > 0:
            nums1[p] = nums2[p2]
            n, p = p2, p - 1
            # nums1[:p2 + 1] = nums2[:p2 + 1]

