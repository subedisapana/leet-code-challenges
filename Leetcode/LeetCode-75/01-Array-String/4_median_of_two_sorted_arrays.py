"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

# Brute Force Approach | time complexity of O(n+m) and O(log(n+m)) | Not effective way
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge_nums =nums1 + nums2
        merge_nums.sort()

        n = len(merge_nums)
        
        if n % 2 == 0: 
            median = float(merge_nums[n // 2] + merge_nums[n // 2 - 1]) / 2
            print(median)
        else:
            median = merge_nums[n // 2]
        return median

soln = Solution()
result = soln.findMedianSortedArrays([1,3], [2])
print(result)

#Two pointer Approach
