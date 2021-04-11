class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected) + 1)]
        priority = [0] * (len(isConnected) + 1)
        components = len(isConnected)
        
        def find(node):
            return node if node == parents[node] else find(parents[node])
        
        def union(start, end):
            
            sParent = find(start)
            eParent = find(end)
            if sParent == eParent:
                return False
                
            if parents[sParent] >= parents[eParent]:
                parents[eParent] = parents[sParent]
                priority[sParent] += 1
            else:
                parents[sParent] = parents[eParent]
                priority[eParent] += 1
            return True
        
        for node, neighbors in enumerate(isConnected):
            for i in range(len(neighbors)):
                if node != i and neighbors[i] == 1:
                    if union(node, i):
                        components -= 1
        return components