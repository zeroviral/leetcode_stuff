# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre_order: List[int]) -> TreeNode:
        iterator = iter(pre_order)
        root = current = TreeNode(next(iterator))
        for val in iterator:
            node = TreeNode(val)
            if node.val < current.val:
                node.right = current
                current.left = current = node
            else:
                while current.right is not None and node.val > current.right.val:
                    current.right, current = None, current.right

                node.right = current.right
                current.right = current = node

        while current.right is not None:
            current.right, current = None, current.right

        return root
        