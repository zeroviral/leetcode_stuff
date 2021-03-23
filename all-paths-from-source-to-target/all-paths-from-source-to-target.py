from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        path = deque([0])
        target = len(graph) - 1
        
        def dfs(node, path):
            if node == target:
                ans.append(list(path))
                return
                
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(nextNode, path)
                path.pop()
        dfs(0, path)
        
        return ans