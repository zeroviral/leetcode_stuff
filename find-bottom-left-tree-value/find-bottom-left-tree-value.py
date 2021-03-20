# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        q = deque()
        q.append(root)
        ans = []
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                if i == 0:
                    ans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans[-1]