# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def dfs(node):
            if not node:
                return
                        
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.left and not node.left.left and not node.left.right:
                if node.left.val == target:
                    node.left = None
            
            if node.right and not node.right.left and not node.right.right:
                if node.right.val == target:
                    node.right = None
            
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        root = dfs(root)
        return root