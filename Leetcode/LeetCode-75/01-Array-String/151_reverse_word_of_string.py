"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)

        # Two pointers approach
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the words
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1

        # Convert the list back to a string
        return ' '.join(s).strip()
        

soln = Solution()
result = soln.reverseWords("the sky is blue")
print(result)