# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(root):
            return dfs(root.left) + [root.val] + dfs(root.right) if root else []

        return sorted(dfs(root1) + dfs(root2))
