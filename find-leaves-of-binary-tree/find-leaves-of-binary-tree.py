# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        lookup = defaultdict(list)

        def dfs(node, layer):
            if not node: 
                return layer 
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            lookup[layer].append(node.val)
            return layer + 1

        dfs(root, 0)
        return lookup.values() 

            