class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        enclaves = 0
        rows, cols = len(A), len(A[0])
        
        def dfs(i, j):
            if not 0 <= i < len(A) or not 0 <= j < len(A[0]) or A[i][j] != 1:
                return
            A[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == len(A) - 1 or col == 0 or col == len(A[0]) - 1 and A[row][col] == 1:
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                enclaves += A[row][col]
        return enclaves