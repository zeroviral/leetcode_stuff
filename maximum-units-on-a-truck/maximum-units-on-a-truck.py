class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        remaining = truckSize
        heap = []
        total = 0
        
        for quantity, size in boxTypes:
            heapq.heappush(heap, (-size, quantity))
        
        while heap:
            boxInfo = heapq.heappop(heap)
            count = min(remaining, boxInfo[1])
            total += count * -boxInfo[0]
            remaining -= count
            
            if remaining == 0:
                break
            
        return total