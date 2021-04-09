# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        diffs = []
        
        def dfs(root):
            if root:
                
                dfs(root.left)
                diffs.append(root.val)
                dfs(root.right)
        
        dfs(root)
        diffs.sort(key = lambda x: abs(x - target))
        
        return diffs[:k]