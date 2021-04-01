class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        
        l = 0
        r = rows
        
        while l < r:
            
            mid = (l + r) // 2
            
            if matrix[mid][0] == target:
                return True
            
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid + 1
        
        targetRow = l - 1
        
        l = 0
        r = cols
        
        while l < r:
            
            mid = (l + r) // 2
            
            if matrix[targetRow][mid] == target:
                return True
            
            elif matrix[targetRow][mid] > target:
                r = mid
            else:
                l = mid + 1
        
        return False
        
        