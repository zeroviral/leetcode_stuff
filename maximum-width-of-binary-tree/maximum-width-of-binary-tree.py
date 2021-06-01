# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        maxWidth = 0
    
        q = collections.deque()
        q.append((0, root))
        
        while q:
            
            length = len(q)
            head = q[0][0]
            
            for i in range(length):
                col, node = q.popleft()
                
                if node.left:
                    q.append((2 * col, node.left))
                if node.right:
                    q.append((2 * col + 1, node.right))
            
            maxWidth = max(maxWidth, col - head + 1)
            
        return maxWidth
            