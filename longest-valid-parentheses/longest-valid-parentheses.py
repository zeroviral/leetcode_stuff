class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0,] # Initial value to handle "()"
        max_parenthesis = 0
        for bracket in s:
            if bracket == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    max_parenthesis = max(max_parenthesis, stack[-1])
                else:
                    stack = [0]

        return max_parenthesis