# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        self.maxDepth = 0
        
        def dfs(root, currDepth=0):
            if not root:
                return
            
            currDepth += 1
            self.maxDepth = max(self.maxDepth, currDepth)
            dfs(root.left, currDepth)
            dfs(root.right, currDepth)
        
        dfs(root)
        return self.maxDepth
            
        