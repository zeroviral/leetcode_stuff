from collections import defaultdict
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        minVal = float('inf')
        lookup = defaultdict(int)
        rows, cols = len(mat), len(mat[0])
        
        for row in range(rows):
            for col in range(cols):
                lookup[mat[row][col]] += 1
        
        for key, value in lookup.items():
            if value >= rows:
                minVal = min(minVal, key)
        
        return minVal if minVal != float('inf') else -1