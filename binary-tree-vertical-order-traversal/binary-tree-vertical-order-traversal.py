# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        lookup = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0))
        
        while q:
            node, column = q.popleft()
            
            if node:
            
                lookup[column].append(node.val)

                if node.left:
                    q.append((node.left, column - 1))
                if node.right:
                    q.append((node.right, column + 1))
        return [lookup[key] for key in  sorted(lookup.keys())]