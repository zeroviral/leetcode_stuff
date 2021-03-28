# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.ans = 0
        
        def dfs(og, cloned):
            if not og:
                return
            dfs(og.left, cloned.left)
            if og == target:
                self.ans = cloned
            dfs(og.right, cloned.right)
        dfs(original, cloned)
        return self.ans