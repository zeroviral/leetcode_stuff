# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def dfs(root, returnVal=0):
            
            if not root:
                return 0
            
            if root.val >= low and root.val <= high:
                returnVal += root.val
            
            return returnVal + dfs(root.left) + dfs(root.right)
        
        return dfs(root)
            