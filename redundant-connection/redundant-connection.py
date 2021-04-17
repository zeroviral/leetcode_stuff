class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        priority = [0] * (len(edges) + 1)
        
        def find(node):
            return parents[node] if parents[node] == node else find(parents[node])
        
        def union(start, end):
            p1, p2 = find(start), find(end)
            if p1 == p2:
                return False
            
            if priority[p1] >= priority[p2]:
                parents[p2] = parents[p1]
                priority[p1] += 1
            else:
                parents[p1] = parents[p2]
                priority[p2] += 1
            return True

        for edge in edges:
            if not union(*edge):
                return edge