"""
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example:
input: word1 = "abc", word2 = "pqr"

Output: "apbqcr"

Explanation: The merged string will be merged as so:

word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged_string = ""
        for i, j in zip(word1,word2):
            merged_string+= i+j 
        merged_string+= word1[len(word2):] + word2[len(word1):] 
        return merged_string

solu = Solution()
result = solu.mergeAlternately("abc", "wxyz")
print(result)