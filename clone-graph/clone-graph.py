"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        1. DFS will be used to traverse the graph
        2. Traverse graph from a given node.
            2.1. Use a hash map to story the reference of the copy of all nodes that have been visited AND cloned.
                2.1.1 The key = node and value = cloned node
        '''
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone = Node(node.val, [])
        self.visited[node] = clone
        
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone
        