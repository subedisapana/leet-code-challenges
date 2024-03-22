
"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            if prefix_sum == total_sum - prefix_sum - num:
                return i
            prefix_sum += num
        
        return -1
    
soln = Solution()
result = soln.pivotIndex([-1,-1,-1,-1,-1,0])
print(result)  