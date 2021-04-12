class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        ans = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                element = matrix[row][col]
                rows[row].append(element)
                cols[col].append(element)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if min(rows[row]) == max(cols[col]):
                    ans.append(matrix[row][col])
        return ans