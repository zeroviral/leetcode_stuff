"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        return deepcopy(root)
        
        