class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] != 'O':
                return 
            grid[row][col] = 'D'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        for row, group in enumerate(grid):
            for col, val in enumerate(group):
                if row in {0, len(grid)-1} or col in {0, len(grid[0])-1} and val == 'O':
                    dfs(row, col)
        
        for row, group in enumerate(grid):
            for col, val in enumerate(group):
                if val == 'D':
                    grid[row][col] = 'O'
                elif val == 'O':
                    grid[row][col] = 'X'