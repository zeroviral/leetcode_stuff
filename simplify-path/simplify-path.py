class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for portion in path.split('/'):
            
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion and portion != '.':
                stack.append(portion)
        
        
        return '/' + '/'.join(stack)