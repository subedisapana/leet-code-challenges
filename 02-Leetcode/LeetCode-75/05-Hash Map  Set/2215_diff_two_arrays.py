"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # index = 0
        # answer= []
        # n1 = len(nums1)
        # distinct_arrays = {0:[]} # index and list of num as value

        # for i in range(n1):
        #     if nums1[i] not in nums2:
        #         distinct_arrays[0].append(nums1[i])  
        #         print(distinct_arrays)
        #         index+=1
        # return distinct_arrays 

        n1 = len(nums1)
        n2 = len(nums2)
        
        distinct_nums1 = {num: True for num in nums1}
        print(distinct_nums1)
        distinct_nums2 = {num: True for num in nums2}
        print(distinct_nums2)
        answer1 = [num for num in nums1 if num not in distinct_nums2]
        print(answer1)
        answer2 = [num for num in nums2 if num not in distinct_nums1]
        print(answer2)

        return [answer1, answer2]


# Alternative way

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        # Find distinct integers in nums1 not present in nums2
        answer1 = list(set_nums1 - set_nums2)
        
        # Find distinct integers in nums2 not present in nums1
        answer2 = list(set_nums2 - set_nums1)

        return [answer1, answer2]

# Example usage:
soln = Solution()
result = soln.findDifference([1,2,3,3], [1,1,2,2])
print(result)  