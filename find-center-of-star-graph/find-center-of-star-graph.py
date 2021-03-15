from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        lookup = defaultdict(list)
        
        for node1, node2 in edges:
            lookup[node1].append(node2)
            lookup[node2].append(node1)
        
        
        for node, connections in lookup.items():
            if len(connections) == len(edges):
                return node