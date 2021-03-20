# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        ans = []
                
        def dfs(root):
            
            if not root:
                return
            
            if root.left and not root.right:
                ans.append(root.left.val)
            elif root.right and not root.left:
                ans.append(root.right.val)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return ans