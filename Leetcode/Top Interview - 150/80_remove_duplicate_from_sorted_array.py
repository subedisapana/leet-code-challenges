
"""
1. Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 

2.The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums

Approach:

1. You can do this in a way where you can append the unique integers to a new array, but while doing this you need additional space for storage.
2. So what we can do is, initialize a index to 0 
    a. iterate via nums
    b. if index < 2: as mentioned you can have at most two repeated integers in an array and
    c. if num is ! =  the num two index behind, if thes condition satisfies:
    d. update the num of that particular index, with new num
    e. increse index by 1
"""




class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 0
        for num in nums:
            if index <2 or num != nums[index-2]:
                nums[index] = num
                print(num, nums[index])
                index+=1
        return index

soln = Solution()
result = soln.removeDuplicates([1,1,1])
print(result)
