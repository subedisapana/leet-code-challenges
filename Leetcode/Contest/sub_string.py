class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[i]== c:
                count+=s[:i+1].count(c)
                
        return count