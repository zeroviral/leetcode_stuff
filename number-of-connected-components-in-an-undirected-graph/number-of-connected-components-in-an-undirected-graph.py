class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        visited = set()
        components = 0
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components