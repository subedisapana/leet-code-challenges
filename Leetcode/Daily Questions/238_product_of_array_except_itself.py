class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # these are two arrays 
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n): # 1,2,3,4
            left[i] = left[i - 1] * nums[i - 1]
        
        # Populate the right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Compute the result array
        answer = [left[i] * right[i] for i in range(n)]
        
        return answer

soln = Solution()
result = soln.productExceptSelf([1,2,3,4])
print(result)

# Alternative way
class Solution(object):

    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result

soln = Solution()
result = soln.productExceptSelf([1,2,3,4])
print(result)