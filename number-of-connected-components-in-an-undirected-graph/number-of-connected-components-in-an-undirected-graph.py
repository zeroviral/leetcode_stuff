class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        1. First create the undirected graph representation in collections.defaultdict(list)
        2. Iterate over the values within a for loop from each node: 0 - n.
            2.1. If we find a node that isn't in our visited set, we DFS on it.
                2.1.1. Within our DFS, first thing we do is add our node into the visited set.
                2.1.2. Then, we iterate over each element in our dictionary[node] (node is input of DFS)
                2.1.3. If we encounter a node outside of visited set, DFS on it.
            2.2. Add one to the total number of components if the component is not in visited.
        3. Return the total # of components.
        '''
        graph = collections.defaultdict(list)
        visited = set()
        components = 0
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components