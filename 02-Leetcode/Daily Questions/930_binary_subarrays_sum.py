"""

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Approach:

1. Initialization:

    total_boxes: 5
    left: 0
    count: 0
    sum_count: {}

2. Loop through the elements: for right in range(total_boxes):current_sum = sum(nums[left:right+1])

 element 1 (right = 0): current_sum = 1
 element 2 (right = 1): current_sum = 1 + 0 = 1
 element 3 (right = 2): current_sum = 1 + 0 + 1 = 2

"""
class Solution():
    def numSubarraysWithSum(self, nums, goal):
       
        left = 0
        count = 0
        curr_sum = 0
        sum_count = {} #sum and number of occurance

        for right in range(len(nums)): # 0,1,2,3,4 (index)
            curr_sum += nums[right]
        
            if curr_sum == goal:
                print("exact 2", right)

                count += 1

            if curr_sum - goal in sum_count:
                print("yes it is in sum_count", right)
                count += sum_count[curr_sum - goal]

            if curr_sum not in sum_count:
                print("not in sum count", right)
                print("curr_sum", curr_sum)
                sum_count[curr_sum] = 1
                print(sum_count)


            else:
                print("else", right)
                sum_count[curr_sum] += 1

        return count

soln = Solution()
result = soln.numSubarraysWithSum([1,0,1,0,1], 2)
print(result) 
