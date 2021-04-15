class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rows, cols = len(matrix), len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                if len(heap) == k:
                    heapq.heappushpop(heap, -matrix[row][col])
                else:
                    heapq.heappush(heap, -matrix[row][col])
        return -heap[0]