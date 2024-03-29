class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        
        def dfs(grid, i, j, count, word):
            
            if count == len(word):
                return True
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != word[count] or grid[i][j] == "0":
                return False
            
            temp = grid[i][j]
            grid[i][j] = "0"
            count += 1
            found = 0
            for row, col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                found += dfs(grid, row, col, count, word)
            grid[i][j] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                    return True
        
        return False
                    