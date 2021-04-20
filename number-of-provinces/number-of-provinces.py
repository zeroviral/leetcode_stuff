class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        provinces = 0
        visited = set()
        
        def dfs(node):
            for index, neighbor in enumerate(isConnected[node]):
                if neighbor == 1 and index not in visited:
                    visited.add(index)
                    dfs(index)
        
        for node in range(len(isConnected)):
            if node not in visited:
                provinces += 1
                dfs(node)
        return provinces