class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = []
        count = 0
        for x, y in points:
            dist = sqrt(x * x + y * y)
            heapq.heappush(maxHeap,([-dist] + points[count]))
            count += 1
        while len(maxHeap)>K:
            heapq.heappop(maxHeap)
        res=[]
        while maxHeap:
            res.append(heappop(maxHeap)[1:])
        return res
        
            
        