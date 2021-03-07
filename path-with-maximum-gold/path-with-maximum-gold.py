class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        self.maxVal = 0
        ans = set()
        
        def dfs(grid, i, j, n, m, total):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            total += grid[i][j]
            temp = grid[i][j]
            grid[i][j] = 0
            currMax = max(total, dfs(grid, i+1, j, m, n, total), dfs(grid, i-1, j, m, n, total), dfs(grid, i, j+1, m, n, total), dfs(grid, i, j-1, m, n, total))
            grid[i][j] = temp
            
            ans.add(currMax)
            return currMax
        
        
        
        n, m = len(grid), len(grid[0])
        
        
        for row in range(n):
            for col in range(m):
                
                if grid[row][col] > 0:
                    self.maxVal = dfs(grid, row, col, n, m, 0)
        
        return max(ans)