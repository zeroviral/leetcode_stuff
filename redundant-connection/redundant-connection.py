class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        def dfs(start, end):
            stack = [start]
            seen = set()
            
            while stack:
                node = stack.pop()
                if node == end:
                    return True
                seen.add(node)
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        stack.append(neighbor)
            return False
        
        graph = collections.defaultdict(list)
        doubles = []
        
        for start, end in edges:
            if start in graph and end in graph:
                if dfs(start, end):
                    doubles.append(start)
                    doubles.append(end)
            graph[start].append(end)
            graph[end].append(start)
        
        return doubles
            