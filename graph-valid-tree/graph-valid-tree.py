class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        priority = [0] * n
        
        def find(node):
            return node if node == parents[node] else find(parents[node])
        
        def union(start, end):
            sParent = parents[start]
            eParent = parents[end]
            if sParent == eParent:
                return False
            if priority[sParent] >= priority[eParent]:
                parents[eParent] = parents[sParent]
                priority[sParent] += 1
            else:
                parents[sParent] = parents[eParent]
                priority[eParent] += 1
            return True
        
        if len(edges) != n - 1:
            return False
        for edge in edges:
            if not union(*edge):
                return False
        return True