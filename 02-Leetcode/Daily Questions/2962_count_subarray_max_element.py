class Solution(object):
    def countSubarrays(self, nums,k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        max_n, max_count = max(nums), 0
        left = 0
        res = 0

        for right in range(n):
            if nums[right] == max_n:
                max_count +=1
            while max_count > k or (left <=right and max_count == k and nums[left]!= max_n): # or max_count == k:
                if nums[left] == max_n:
                    max_count -= 1
                left+=1
            if max_count == k:
                res += left+1
        return res

soln = Solution()
result = soln.countSubarrays([1,3,2,3,3], 2)
print(result)
        
# Another Way

class Solution:
    def countSubarrays(self, nums, k):
        max_val = max(nums)
        res = 0
        left = 0
        count = 0
        for num in nums:
            if num == max_val:
                count += 1

            while count >= k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            res += left
            
        return res

soln = Solution()
result = soln.countSubarrays([1,3,2,3,3], 2)
print(result)