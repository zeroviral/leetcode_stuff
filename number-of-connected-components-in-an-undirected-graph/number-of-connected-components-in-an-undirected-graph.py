class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        components = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1
        return components