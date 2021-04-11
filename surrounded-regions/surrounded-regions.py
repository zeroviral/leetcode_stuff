class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] != 'O':
                return 
            grid[row][col] = 'D'
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(i, j)
        
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1 and grid[row][col] == 'O':
                    dfs(row, col)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'D':
                    grid[row][col] = 'O'
                elif grid[row][col] == 'O':
                    grid[row][col] = 'X'