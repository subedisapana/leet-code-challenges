"""
You are given two strings order and s.
1. order contains unique characters that are sorted in a specific order.
2. s is any string containing characters.

Your task is to permute the characters of s so that they follow the same order as the characters in order. This means:

If a character x occurs before a character y in order, then x should occur before y in the permuted string.
However, it doesn't mean that all characters in order must appear in s, or vice versa. You just need to maintain the relative order of the characters that do appear.

Example 1:

Input:  order = "cba", s = "abcd" 

Output:  "cbad" 

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
"""

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        result = ""

        for i in order:
            if i in s: 
                result += i * s.count(i) 
                s = s.replace(i, "")
        result += s 
        return result


soln = Solution()
result = soln.customSortString("cbae","abedcafc" )
print(result)