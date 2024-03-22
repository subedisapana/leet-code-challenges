from math import sqrt


class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = sqrt(n * (n + 1) / 2)
        
        if x % 1 != 0:
            return -1
        else:
            return int(x)

soln = Solution()
result = soln.pivotInteger(8)
print(result)

# Alternative Way

class Solution(object):
    def pivotInteger(self, n):
        left_value, right_value = 1, n
        left_sum, right_sum = left_value, right_value

        if n == 1:
            return 1

        while left_value < right_value:
            if left_sum < right_sum:
                left_value += 1
                left_sum += left_value
            else:
                right_value -= 1 
                right_sum += right_value
            
            if left_sum == right_sum and left_value+1 == right_value-1:
                return left_value+1

        return -1

soln = Solution()
result = soln.pivotInteger(8)
print(result)
