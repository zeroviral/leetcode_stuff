class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        pri = [0] * (len(edges) + 1)
        
        def find(node):
            return node if node == parents[node] else find(parents[node])
        
        def union(start, end):
            p1, p2 = find(start), find(end)
            
            if p1 == p2:
                return False
            if parents[p1] >= parents[p2]:
                parents[p2] = parents[p1]
                pri[p1] += 1
            
            parents[p1] = parents[p2]
            pri[p2] += 1
            return True
        
        for edge in edges:
            if not union(*edge):
                return [*edge]