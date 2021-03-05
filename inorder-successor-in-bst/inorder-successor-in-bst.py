# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        curr = root
        candidate = None
        while curr:
            
            if curr.val > p.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right
        
        return candidate
        
        
        
        
        
        
        
        
        
        