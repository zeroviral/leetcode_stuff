class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j, m, n):
            
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j, m, n)
            dfs(grid, i - 1, j, m, n)
            dfs(grid, i, j + 1, m, n)
            dfs(grid, i, j - 1, m, n)
            
        
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j, m, n)
        
        return count