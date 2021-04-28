class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        1. Exhaust all possibilities with ladders first
        
        '''
        heap = []
        for i in range(len(heights) - 1):
            climbDiff = heights[i + 1] - heights[i]
            
            if climbDiff <= 0:
                continue
            
            heapq.heappush(heap, climbDiff)
            
            if len(heap) <= ladders:
                continue
            
            bricks -= heapq.heappop(heap)
            
            if bricks < 0:
                return i
        
        return len(heights) - 1