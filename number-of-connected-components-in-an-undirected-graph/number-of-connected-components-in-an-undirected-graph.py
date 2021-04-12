class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        components = 0
        seen = set()
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        
        
        for node in range(n):
            if node not in seen:
                components += 1
                dfs(node)
        return components