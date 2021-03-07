class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j, total):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            total += grid[i][j]
            temp = grid[i][j]
            grid[i][j] = 0
            currMax = max(total, dfs(grid, i + 1, j, total),
                          dfs(grid, i - 1, j, total),
                          dfs(grid, i, j + 1, total),
                          dfs(grid, i, j - 1, total))
            grid[i][j] = temp
            return currMax

        maxVal = 0

        for row in range(len(grid)):
            for col in range((len(grid[0]))):

                if grid[row][col] > 0:
                    maxVal = max(maxVal, dfs(grid, row, col, 0))

        return maxVal