class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # if there are multiple spaces, split treats them as a single separator, ignoring the leading and trailing spaces.
        words = s.split()
        print(words)

        if len(words) == 0:
            return 0
        return len(words[-1])


s = "   fly me   to   the moon  "
soln = Solution()
result = soln.lengthOfLastWord(s)
print(result)
