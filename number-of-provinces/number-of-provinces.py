class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        provinces = 0
        visited = set()
        
        def dfs(node):
            for curr, neighbors in enumerate(isConnected[node]):
                if neighbors and curr not in visited:
                    visited.add(curr)
                    dfs(curr)
        
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        return provinces