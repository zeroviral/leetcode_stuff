class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path.copy())
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        
        
        dfs(0, [0])
        return ans
            