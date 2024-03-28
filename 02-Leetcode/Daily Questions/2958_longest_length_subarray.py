"""
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict

class Solution():
    def maxSubarrayLength(self, nums,k):
        left = 0
        max_length = 0
        element_frequency = defaultdict(int)
        
        for right in range(len(nums)):
            element_frequency[nums[right]] += 1
            
            while element_frequency[nums[right]] > k:
                element_frequency[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        

soln = Solution()
result = soln.maxSubarrayLength([5,10,2], 4)
print(result)

