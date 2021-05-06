class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or not grid[i][j] or (i, j) in seen:
                return
            seen.add((i, j))
            currIsland.add((i - row, j - col))
            
            for a, b in [(i+1, j), (i-1, j), (i, j+1), (i,j-1)]:
                dfs(a, b)
            
            
        
        seen = set()
        unique_islands = set()
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                currIsland = set()
                dfs(row, col)
                if currIsland:
                    unique_islands.add(frozenset(currIsland))
        return len(unique_islands)