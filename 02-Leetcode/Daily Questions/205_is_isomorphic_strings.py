"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapping = {}
        mapped_chars = set()
    
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapped_chars:
                    return False
                mapping[s[i]] = t[i]
                mapped_chars.add(t[i])
            elif mapping[s[i]] != t[i]:
                return False
        
        return True
        
soln = Solution()
result = soln.isIsomorphic("egg", "add")
print(result)