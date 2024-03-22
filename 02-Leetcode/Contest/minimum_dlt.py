class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
        count={}
        for w in word:
            if w in count:
                count[w]+=1
            else:
                count[w] = 1
                
        
        max_count = max(count.values())
        deletions =0
        
        for value in count.values():
            if max_count - value > k:
                deletions+=value
        return deletions
        
        
        
        
# Test cases
soln = Solution()
result2 = soln.minimumDeletions("dabdcbdcdcd",
2)
print(result2)  
