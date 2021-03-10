# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if not root:
            return root
        
        q = deque()
        q.append(root)
        returnList = []
        
        while q:
            currRow = []
            for i in range(len(q)):
                node = q.popleft()
                currRow.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            returnList.append(currRow)
        
        ans = []
        
        for element in returnList:
            average = sum(element) / len(element)
            ans.append(average)
        
        return ans
        