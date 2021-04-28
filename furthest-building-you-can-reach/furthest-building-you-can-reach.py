class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        1. Create a heap = []
        2. Iterate through the list, up until the len(heights) - 1 element.
            2.1. Calculate the diff of the next element minus the current element
                2.1.1. If the diff is less than 0, continue.
                2.1.2. If the diff is greater than 0, we need to use bricks.
                2.1.3. Push the -diff onto the heap (we're using a max heap)
                2.1.4. return the index if the bricks is < 0 and ladders == 0
                2.1.5. If ONLY BRICKS < 0, we'll add bricks += -heap.heappop()
                    2.1.5.1. Minus one from the ladders
        3. If we didn't return in the loop above, we'll return the last index since we can travel to the end.
                
        
        '''
        heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:
                continue
            
            bricks -= diff
            heapq.heappush(heap, -diff)
            
            if bricks < 0 and ladders == 0:
                return i
            
            if bricks < 0:
                bricks += -heapq.heappop(heap)
                ladders -= 1
        return len(heights) - 1