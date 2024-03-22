class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        
        # Add all intervals that come after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

soln = Solution()
result = soln.insert([[1,3],[6,9]], [2,5])
print(result)


# Another way

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l,r = [], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                l.append(interval)
            elif interval[0] > newInterval[1]:
                r.append(interval)
            else:
                newInterval = (min(interval[0], newInterval[0]),max(interval[1], newInterval[1]))
        return l + [newInterval] + r

        