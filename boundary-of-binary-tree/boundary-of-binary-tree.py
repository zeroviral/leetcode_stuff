# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        

        def getLeftBoundaries(curr):
            
            #Summary: get most left, if there are not lefts, check if there is right
            if curr and (curr.left or curr.right):
                result.append(curr.val)
            if curr.left:
                getLeftBoundaries(curr.left)
            elif curr.right:
                getLeftBoundaries(curr.right)
            return

        def getRightBoundaries(curr):
            if curr.right:
                getRightBoundaries(curr.right)
            elif curr.left:
                getRightBoundaries(curr.left)
            if curr and (curr.left or curr.right):
                result.append(curr.val)


        #list of leaf Nodes
        def getLeafNodes(curr):

            if not curr.left and not curr.right:
                result.append(curr.val)

            if curr.left:
                getLeafNodes(curr.left)

            if curr.right:
                getLeafNodes(curr.right)

        result = []
 

        if root:
            result.append(root.val)

            # the root's left
            if root.left:
                getLeftBoundaries(root.left)
                getLeafNodes(root.left)

            # the root's right
            if root.right:
                getLeafNodes(root.right)
                getRightBoundaries(root.right)

        return result