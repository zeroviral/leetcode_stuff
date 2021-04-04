# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.currSum = 0
        
        def dfs(root):
            
            if root:
                dfs(root.right)
                root.val += self.currSum
                self.currSum = root.val
                dfs(root.left)
        dfs(root)
        return root