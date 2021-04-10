class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        self.path = math.inf
        indegrees = collections.defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            indegrees[end].append(start)
        
        ans = []
        for node in graph.keys():
            if node not in indegrees:
                ans.append(node)
        
        return ans