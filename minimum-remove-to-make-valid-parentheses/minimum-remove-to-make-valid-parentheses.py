class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Needs - Removal set, stack.
        The main idea is we want to record the index positions that are going to be in the returnString.
        1. Iterate through the string and check to see if each element is in '()'
            1.1. If the character isn't in the '()', we need to continue (skip to next position)
            1.2. If the character is a '(' we need to append it to our stack.
            1.3. If the character is a ')':
                1.3.1. If the stack is not empty, we will pop cause it matches a parenthesis.
                1.3.2. If the stack is empty we need to add the position to our removals set - it won't be in the returnString
            1.4. Create a union set of the stack, and the removals set. This will show which positions we can't use.
        2. Iterate through the input string, and add each c if c not in removals set.
        3. Return the recomposed string.
        '''
        removals = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                removals.add(i)
            else:
                stack.pop()
        removals |= set(stack)
        return "".join([c for i, c in enumerate(s) if i not in removals])