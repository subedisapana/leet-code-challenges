class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen_once = set()
        duplicates = set()
        
        for num in nums:
            if num in seen_once:
                duplicates.add(num)
            else:
                seen_once.add(num)
        
        return list(duplicates)
        
# Another way (consume less memory)

class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
        
        return duplicates
