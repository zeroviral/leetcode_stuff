"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if len(tree) == 1:
            return tree[0]
        parents = collections.defaultdict(list)
        children = set()
        
        for node in tree:
            if node.children:
                for child in node.children:
                    parents[node].append(child) 
                    children.add(child)
        
        for key in parents.keys():
            if key not in children:
                return key