"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# Given the node, check if it has right child - if it does, traverse right, then as far left as possible
# If it doesn't have a right child, go up to parent until parent doesn't exist anymore.
# Record values on the way up and down
# Check if something >= node.val + 1 exists in the records. Return it if true, otherwise return null

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node == node.parent.right:
            node = node.parent
        
        return node.parent
    