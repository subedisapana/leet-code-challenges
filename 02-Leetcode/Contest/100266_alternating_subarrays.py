def count_alternating_subarrays(nums):
    count = 0  # Initialize the count of alternating subarrays
    start = 0   # Initialize the start index of the current subarray

    # Iterate through the array
    for end in range(len(nums)):
        # Check if the current element violates the alternating condition
        if end > 0 and nums[end] == nums[end - 1]:
            start = end  # Reset the start index to the current position
        
        # Increment the count by the length of the current subarray
        count += end - start + 1

    return count

# Example usage:
nums1 = [0, 1, 1, 1]
print(count_alternating_subarrays(nums1))  # Output: 5

