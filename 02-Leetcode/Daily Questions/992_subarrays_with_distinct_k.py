class Solution:
    def subarraysWithKDistinct(nums, k):
        def at_most_k(nums, k):
            count = 0
            left = 0
            num_count = {}
            distinct_count = 0

            for right in range(len(nums)):
                num_count[nums[right]] = num_count.get(nums[right], 0) + 1

                if num_count[nums[right]] == 1:
                    distinct_count += 1

                while distinct_count > k:
                    num_count[nums[left]] -= 1
                    if num_count[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return at_most_k(nums, k) - at_most_k(nums, k - 1)
