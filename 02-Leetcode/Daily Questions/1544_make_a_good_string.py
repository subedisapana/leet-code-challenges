class Solution(object):
    def makeGood(self, s):
        stack = []

        for char in s:
            # Check if the stack is not empty and the current character forms a bad pair with the top of the stack
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()  # Remove the top character from the stack
            else:
                stack.append(char)  # Push the current character onto the stack
        
        return ''.join(stack)  # Join the characters remaining in the stack to form the result string



soln = Solution()
result = soln.makeGood("LeeeEtcode")
print(result)
