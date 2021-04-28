# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode: 
        
        def dfs(arr):
            
            if not arr:
                return
            
            pivot = arr.index(max(arr))
            root = TreeNode(arr[pivot])
            root.left = dfs(arr[:pivot])
            root.right = dfs(arr[pivot + 1:])
            
            return root
        
        return dfs(nums)