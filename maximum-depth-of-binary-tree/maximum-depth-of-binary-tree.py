# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        self.maxDepth = 0
        
        def dfs(root, currDepth=1):
            
            if not root:
                return 0
            
            self.maxDepth = max(self.maxDepth, currDepth)
            print(currDepth)
            dfs(root.left, currDepth + 1)
            dfs(root.right, currDepth + 1)
        
        dfs(root)
        return self.maxDepth
        