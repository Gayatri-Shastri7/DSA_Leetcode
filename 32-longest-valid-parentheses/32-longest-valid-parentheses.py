class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        stack = []
        dp = [0]*len(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                dp[i] = 0
            else: #we have a closing brace
                if len(stack) == 0:
                    dp[i] = 0
                else:
                    pos = stack.pop()
                    dp[i] = dp[pos-1]+i-pos+1
        return max(dp)
    '''
    Simply iterate through the string.
If s[i] == "(" simply store the position in the stack, and dp[i] = 0 (because it does not signify the end of any valid parentheses. The position in stack will be used to check if the string made is completed or not later.
Now, if s[i] == ")" see if the length of stack > 0, if it is not, dp[i] = 0 because no valid parentheses end there. if length > 0, then pop the top of the stack, that is the position of the "(" that completes the current ")".
Now, just check if there was any valid parentheses ending just before that position. Because, if there was, this should be added to our length of the valid parentheses.
eg:
()(())
dp = [0, 2, 0, 0, 2, 6]
Here, for the last ) at position 5, it gets completed by the ( at position 2, now check position 1, if there is a valid parentheses ending there, add its length to the current length.

The code is below:
    '''