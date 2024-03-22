"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Approach:
1.Since you have to alter the vowels present, initialize two pointers indicating left most and right most char os the string.
2.Until when left < right pointer, Check whether the left and right index char is in vowels or not.
3.If yes, move to the next index.
4.If char represented by left pointer is not in vowels, then increse the left pointer by 1.
5.Similarly, if char indicting by right pointer is not in vowels, then decrease the right pointer by 1
6.At last, convert list back to string using join.

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        left, right = 0, len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] not in vowels:
                left+=1
            else:
                right-=1
        
        return ''.join(s)

soln = Solution()
result = soln.reverseVowels("LeetCode")
print(result)
        