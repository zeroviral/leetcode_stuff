"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        self.maxDepth = 0
        
        def dfs(root, currDepth=0):
            if not root:
                return 0
            
            currDepth += 1
            self.maxDepth = max(self.maxDepth, currDepth)
            for child in root.children:
                dfs(child, currDepth)
        
        dfs(root)
        return self.maxDepth
        