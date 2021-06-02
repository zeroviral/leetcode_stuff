# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        cur_layer = [(root, 0, 0)]
        res = 0
        while cur_layer:
            next_layer = []
            for node, left, right in cur_layer:
                res = max(res, left, right)
                if node.left:
                    next_layer.append((node.left, right+1, 0))
                if node.right:
                    next_layer.append((node.right, 0, left+1))
            cur_layer = next_layer
            
        return res