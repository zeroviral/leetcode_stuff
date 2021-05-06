class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for a, b in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                dfs(a,b)
        
        islands = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        return islands