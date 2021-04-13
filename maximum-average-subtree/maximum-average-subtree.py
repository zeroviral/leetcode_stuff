# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        self.res = 0
        
        def dfs(root):
            
            if not root:
                return [0, 0]
            
            # Calculate left subtree
            left_sum, leftChildren = dfs(root.left)
            
            # Calculate right subtree
            right_sum, rightChildren = dfs(root.right)
            
            currSum = left_sum + right_sum  + root.val
            currChildNum = 1 + leftChildren + rightChildren
            
            
            self.res = max(self.res, currSum/currChildNum)
            
            return [currSum, currChildNum]
        
        dfs(root)
        
        return self.res