"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 """
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_open, count_close, count_ast = 0,0,0
        hash_map = {}
        for i, char in enumerate(s):
            if char == '(':
                count_open += 1
                hash_map[char] = count_open
            elif char == ')':
                count_close += 1
                hash_map[char] = count_close
            elif char == '*':
                count_ast += 1
                hash_map[char] = count_ast
        print(hash_map)
        if count_open == count_close:
            return True
        elif abs(count_open - count_close) == count_ast:
            return True
        return False

        
soln = Solution()
result = soln.checkValidString('(*)')
print(result)

# Alternative Way4
class Solution(object):
    def checkValidString(self, s):
        min_open = max_open = 0
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open = max(min_open - 1, 0)
                max_open -= 1
                if max_open < 0:
                    return False
            else:  # char == '*'
                min_open = max(min_open - 1, 0)
                max_open += 1
        return min_open == 0