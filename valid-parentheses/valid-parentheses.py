class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '[':']',
            '{':'}',
            '(':')'
        }
        stack = []
        for element in s:
            if element in lookup:
                stack.append(element)
            elif len(stack) == 0 or lookup[stack.pop()] != element:
                return False
        return len(stack) == 0
            