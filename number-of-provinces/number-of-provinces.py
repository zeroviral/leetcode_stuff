class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        provinces = 0
        visited = set()
        
        def dfs(node):
            for curr, nxt in enumerate(isConnected[node]):
                if nxt and curr not in visited:
                    visited.add(curr)
                    dfs(curr)
        
        
        components = 0
        for i in range(len(isConnected)):
            if i not in visited:
                components += 1
                dfs(i)
        return components
        
        