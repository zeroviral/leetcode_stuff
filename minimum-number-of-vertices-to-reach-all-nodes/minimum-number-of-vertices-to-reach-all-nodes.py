class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        destinations = [0] * n
        
        for start, end in edges:
            graph[start].append(end)
            destinations[end] = 1
        
        return [node for node in graph.keys() if destinations[node] == 0]