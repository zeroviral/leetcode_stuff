# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        
        if not root:
            return root
        
        q = deque()
        q.append(root)
        returnList = []
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Here we simply add the final node value that was popped once outside the for loop
            returnList.append(node.val)
        
        return returnList
        
        