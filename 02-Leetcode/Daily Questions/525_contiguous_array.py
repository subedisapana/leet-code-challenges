"""
Given a binary array nums, 
return the maximum length of a contiguous  
with an equal number of 0 and 1.

[0,1,0]
1. longest length
2. sub array with equal no. of 0 and 1
[0,1] or [1,0]

Hashmap: It is also called dict.It stores key-value pair.
1. Initialization:
The hashmap is initialized with {0: -1} where the key represents the cumulative sum at that point,
and the value represents the index where this sum was first encountered. 
This initialization is crucial as it handles the case when there are equal numbers of 0s and 1s from the beginning.

2.For each count value encountered during iteration, 
the code checks if that count value is already present in the hashmap. 
If it is, it calculates the length of the  with equal 0s and 1s by taking the difference between the current index i and the index stored in the hashmap for that count. This helps in finding s with equal numbers of 0s and 1s.

"""

def findMaxLength(nums):
    count = 0
    max_length = 0
    hashmap = {0: -1} # Key reperesent cumulative sum and value is the index.

    for i in range(len(nums)): # 0
        if nums[i] == 1:
            count += 1 
        else:
             count -= 1

        if count in hashmap:
            max_length = max(max_length, i - hashmap[count])
        else:
            hashmap[count] = i

    return max_length

nums = [0, 1,1,0,1,0 ,0]
print(findMaxLength(nums)) 
