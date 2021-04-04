# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        self.smallest = math.inf
        self.ans = 0
        
        def dfs(root):
            if root:
                
                if abs(root.val - target) < self.smallest:
                    self.smallest = abs(root.val - target)
                    self.ans = root.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.ans
        
        