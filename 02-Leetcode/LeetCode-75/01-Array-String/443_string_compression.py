"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 0
        count_map = {} # word and 
        s = []
        n = len(chars)

        for i in range(n):
            if i in s and i < n:
                count+=1
                print(i)
                # if count == 10:
                #     s[i+1] = 10
                #     print("already 10")
                # else:
                #     s[i+1] = count
            else:
                # print(s[i], chars[i])
                # s[i] = chars[i]
                count+=1
        
soln = Solution()
result = soln.compress(["a","a","b","b","c","c","c"])
print(result)
