class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}  # Stores the count of each number

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1 # {2: 1} # number and sum

        n = len(nums) // 2

        for num, count in count_map.items():
            if count > n:
                return num
        return num
                
        



soln = Solution()
result = soln.majorityElement([2,2,1,1,1,2,2])
print(result)
