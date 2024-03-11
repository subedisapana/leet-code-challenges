"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if req_num in result:
                return[result[req_num], i]
            result[nums[i]] = i

soln = Solution()
result = soln.twoSum([2,7,11,15], 17)
print(result)
        

# Alternative way        

class Solution(object):
    def twoSum(self, nums, target): 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return 'None'

soln = Solution()
result = soln.twoSum([2,7,11,15], 17)
print(result)