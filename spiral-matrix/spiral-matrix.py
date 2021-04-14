class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        turn = 0
        
        while len(matrix) != 0 and len(matrix[0]) != 0:
            if turn % 4 == 0: # need to pop first row
                res += matrix.pop(0)
                
            if turn % 4 == 1: # need to pop last column
                for i in range(len(matrix)):
                    res.append(matrix[i].pop())

            if turn % 4 == 2: # need to pop last row and reverse
                res += matrix.pop()[::-1]
                
            if turn % 4 == 3: # need to pop first column and reverse
                for i in range(len(matrix))[::-1]:
                    res.append(matrix[i].pop(0))

            turn += 1

        return res