class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []
        n =len(nums)
        for i in range(n): # 0,1,2,3
            if i < 2:
                if i == 0: 
                    arr1.append(nums[i]) 
                else:
                    arr2.append(nums[i]) 
            else:
                if arr1[-1] > arr2[-1]:
                    print("range", arr1[:-1], )
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

        return  [y for x in [arr1, arr2] for y in x]


soln = Solution()
result = soln.resultArray([5,4,3,8])
print(result)