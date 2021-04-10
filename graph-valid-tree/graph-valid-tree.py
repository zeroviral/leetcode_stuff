class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        lookup = collections.defaultdict(list)
        stack = []
        seen = set()
               
        for node, neighbor in edges:
            lookup[node].append(neighbor)
            lookup[neighbor].append(node)
        
        stack.append(0)
        parent = {0 : -1}
        
        while stack:
            node = stack.pop()
            for neighbor in lookup[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                stack.append(neighbor)
        
        return len(parent) == n