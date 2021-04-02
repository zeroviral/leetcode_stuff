class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix) - 1, 0
        height, width = len(matrix), len(matrix[0])
        
        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False