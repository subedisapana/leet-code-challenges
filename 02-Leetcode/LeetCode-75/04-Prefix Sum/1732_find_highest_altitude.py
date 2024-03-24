"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        sum_alt = 0
        max_alt = 0
        for i in range(0, len(gain)):
            sum_alt = sum_alt + gain[i]
            max_alt = max(sum_alt, max_alt)
        return max_alt
        
soln = Solution()
result = soln.largestAltitude([-4,-3,-2,-1,4,3,2])
print(result)