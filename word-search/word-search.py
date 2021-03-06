class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(grid, i, j, count, target):
            
            if count == len(target):
                return True
            
            if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[i]) or grid[i][j] != target[count]:
                return False
            
            temp = grid[i][j]
            grid[i][j] = ''
            found = dfs(grid, i+1, j, count + 1, target) or dfs(grid, i-1, j, count + 1, target) or dfs(grid, i, j+1, count + 1, target) or dfs(grid, i, j-1, count + 1, target)
            board[i][j] = temp
            
            return found
        
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                    return True
        
        return False