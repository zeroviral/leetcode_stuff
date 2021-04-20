"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        
        def dfs(root):
            depths = [0, 0]
            for child in root.children:
                depths.append(dfs(child))
            self.ans = max(self.ans, sum(sorted(depths, reverse=True)[:2]))
            return max(depths) + 1

        dfs(root)
        return self.ans