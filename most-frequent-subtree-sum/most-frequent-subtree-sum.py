# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        self.lookup = defaultdict()
        def dfs(root):
            
            if not root:
                return 0
            
            total = dfs(root.left) + dfs(root.right) + root.val
            
            if total in self.lookup:
                self.lookup[total] += 1
            else:
                self.lookup[total] = 1
            
            return total
        
        dfs(root)
        maxVal = max(self.lookup.values())
        
        return [key for key, value in self.lookup.items() if value == maxVal]
