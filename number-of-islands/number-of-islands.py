class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(grid, a, b)
        
        for row in range(rows):
            for col in range(cols):        
                if grid[row][col] == '1':
                    count += 1
                    dfs(grid, row, col)
        return count