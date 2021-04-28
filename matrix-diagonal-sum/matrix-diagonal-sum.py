class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        total = 0
        visited = set()
        
        row, col = 0, 0
        
        while row <= rows - 1 and col <= cols - 1:
            if (row, col) not in visited:
                visited.add((row, col))
                total += mat[row][col]
            col += 1
            row += 1
        
        col = 0
        row = len(mat) - 1
        while row >= 0 and col <= cols - 1:
            if (row, col) not in visited:
                visited.add((row, col))
                total += mat[row][col]
            col += 1
            row -= 1
        
        return total
        
        
            
                