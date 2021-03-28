from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        path = deque()
        path.append(0)
        target = len(graph) - 1
        
        def dfs(node, path):
            
            
            if node == target:
                ans.append(list(path))
                return
            print(f'its currently lookin like: dqeue: {path}')
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(nextNode, path)
                path.pop()
        dfs(0, path)
        return ans
    