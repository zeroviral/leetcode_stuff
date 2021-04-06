class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        
        def dfs(node):
            for curr, nxt in enumerate(isConnected[node]):
                if nxt and curr not in seen:
                    seen.add(curr)
                    dfs(curr)
        
        
        components = 0
        for i in range(len(isConnected)):
            if i not in seen:
                components += 1
                dfs(i)
        return components
                