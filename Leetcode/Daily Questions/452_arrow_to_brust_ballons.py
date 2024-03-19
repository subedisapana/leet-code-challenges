"""
here are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # arrow_count = 1 # because we alz need at least 1 arrow

        # if not points:
        #     return 0

        # sorted_arr = sorted(points) # [[1, 6], [2, 8], [7, 12], [10, 16]]
        # curr_end = points[0][1]
        
        # for start, end in sorted_arr:
        # # If current balloon's start point is beyond the current end point,
        # # we need a new arrow
        #     if start > curr_end:
        #         arrow_count += 1
        #         curr_end = end  # Update the current end point
        # return arrow_count
            # Sort balloons based on end points
        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_end = points[0][1]

        # Iterate through balloons
        for start, end in points:
            # If current balloon's start point is beyond the current end point,
            # we need a new arrow
            if start > curr_end:
                arrows += 1
                curr_end = end  # Update the current end point
        return arrows
            
        
soln =Solution()
result = soln.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(result)