class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        distances = {node : math.inf for node in range(1, N + 1)}

        for start, end, weight in times:
            graph[start].append((weight, end))
        
        def dfs(node, totalTime):
            if totalTime >= distances[node]:
                return
            distances[node] = totalTime
            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, totalTime + time)
        
        dfs(K, 0)
        ans = max(distances.values())
        return ans if ans < math.inf else -1
                