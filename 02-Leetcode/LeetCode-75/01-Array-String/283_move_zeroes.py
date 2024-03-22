"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution():
    def removeZeroes(self, nums):

        index =0
        j= len(nums)-1

        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[index] = nums[i]
                index+=1

        while index < len(nums):
            nums[index] = 0
            index += 1
            
        return nums
            

soln = Solution()
result = soln.removeZeroes([0,1,0,3,12])
print(result)