class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''Needs - Removal set, stack.
        1. Iterate through list, find parenthesis
        2. Check parenthesis type
            2.1 If parenthesis is ( then append to stack
            2.2 if Parenthesis is ) then
                2.2.1 if stack is empty add index to removals set
                2.2.2 if stack not empty then append pop from the stack
        3. Combine the stack and removals set
        4. Return string composed of all characters not in the union set
        '''
        removals = set()
        stack = []
        
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif c == ")" and not stack:
                removals.add(i)
            else:
                stack.pop()
        removals = removals.union(set(stack))
        return "".join([c for i, c in enumerate(s) if i not in removals])
        
        