from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        lookup = defaultdict(list)
        path = []
        for start, end in paths:
            lookup[start].append(end)
            path.append(start)
            path.append(end)
        
        for item in path:
            if item not in lookup:
                return item