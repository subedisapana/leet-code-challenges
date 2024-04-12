"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set()
        
        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            else:
                hash_set.add(num)
            
        return  hash_set.pop()
                
soln = Solution()
result = soln.singleNumber([1,2,3,3])
print(result)
            
