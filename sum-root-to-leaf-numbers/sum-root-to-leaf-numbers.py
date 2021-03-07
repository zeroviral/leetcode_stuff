# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(root, path=""):
            
            if not root:
                return 0
            
            if root.left is None and root.right is None:
                path += str(root.val)
                return int(path)
            
            
            path += str(root.val)
            return dfs(root.left, path) + dfs(root.right, path)
            
        
        return dfs(root)
        
        
            