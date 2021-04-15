class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        '''
        1. Create a graph from collections.defaultdict that contains mappings for every node. (Adjacency list)
            1.1. Create a visited set.
            1.2. Populate the graph with undirected nodes
            1.3. Keep track of components (if there is more than one at the end, we return -1)
                1.3.1. Add up weights of paths, maintain max(curr_path, longest_path)
        2. Return the maxPath if components == 1 otherwise return -1
        '''
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
                