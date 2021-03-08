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
                return 0
            
            currDepth +=1
            self.maxDepth = max(currDepth, self.maxDepth)
            dfs(root.left, currDepth)
            dfs(root.right, currDepth)
            
            return currDepth
        
        dfs(root)
        
        return self.maxDepth
        