from sortedcontainers import SortedList

class Solution:
    def minimumDistance(self, points):
        a, b = SortedList(), SortedList()
        n = len(points)
        for i in range(n):
            a.add(points[i][0] + points[i][1])
            b.add(points[i][0] - points[i][1])
        res = float('inf')
        for i in range(n):
            a.remove(points[i][0] + points[i][1])
            b.remove(points[i][0] - points[i][1])
            res = min(res, max(a[-1] - a[0], b[-1] - b[0]))
            a.add(points[i][0] + points[i][1])
            b.add(points[i][0] - points[i][1])
        return res

# Example usage:
solution = Solution()
points = [[1,2],[3,4],[6,1]]
print(solution.minimumDistance(points))  # Output will vary based on input
