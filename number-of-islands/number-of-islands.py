class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for i, j in [(i+1, j), (i-1, j), (i, j+1), (i,j-1)]:
                dfs(i,j)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands