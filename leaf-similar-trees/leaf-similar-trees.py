# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        leaves1, leaves2 = [], []
        
        def dfs(root, container):
            if not root:
                return
            
            dfs(root.left, container)
            
            if not root.left and not root.right:
                container.append(root.val)
        
            dfs(root.right, container)
        
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        
        return leaves1 == leaves2