# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root.val % 2 == 0:
            return False
        ans = []
        
        q = deque()
        q.append(root)
        while q:
            
            row = []
            for i in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row)
            
        
        for i in range(len(ans)):
            
            if len(ans[i]) == 1:
                if i % 2 == 0:
                    if ans[i][0] % 2 == 0:
                        return False
                if i % 2 == 1:
                    if ans[i][0] % 2 != 0:
                        return False
            
            for j in range(1, len(ans[i])):
                curr, prev = ans[i][j], ans[i][j - 1]
                if i % 2 == 0:
                    if curr <= prev or curr % 2 == 0:
                        return False
                else:
                    if curr >= prev or curr % 2 != 0:
                        return False
        return True
                