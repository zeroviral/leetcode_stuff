# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            maxVal = -math.inf
            for _ in range(len(q)):
                node = q.popleft()
                maxVal = max(maxVal, node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maxVal)
        return ans