# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        self.minVal = float('inf')
        self.topDiff = float('inf')
        
        def dfs(root):
            
            if not root:
                return 
            
            if abs(target - root.val) < self.topDiff:
                self.topDiff = abs(target - root.val)
                self.minVal = root.val
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        
        return self.minVal