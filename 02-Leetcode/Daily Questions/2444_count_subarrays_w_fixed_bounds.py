"""You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array."""

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        res = 0
        min_i = max_i = outof_i = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                outof_i = i
            if nums[i] == minK:
                min_i = i
            if nums[i] == maxK:
                max_i = i
            temp = min(max_i, min_i) - outof_i
            res += max(0, temp)
        return res

soln = Solution()
result = soln.countSubarrays([1,3,5,2,7,5], 1, 5)
print(result)
