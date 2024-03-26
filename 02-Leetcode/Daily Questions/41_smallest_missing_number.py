class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        filtered_set = set()
        for num in nums:
            if num>0:
                filtered_set.add(num)

        for i in range(1, len(filtered_set) + 2):
            if i not in filtered_set:
                return i

soln = Solution()
result = soln.firstMissingPositive([3,4,-1,1])
print(result)
        