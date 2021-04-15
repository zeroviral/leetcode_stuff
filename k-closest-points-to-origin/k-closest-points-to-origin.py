class Solution(object):
    def kClosest(self, points, K):
        minHeap = []
        
        for x, y in points:
            distance = -(x*x + y*y)
            if len(minHeap) == K:
                heapq.heappushpop(minHeap, (distance, (x,y)))
            else:
                heapq.heappush(minHeap, (distance, (x,y)))
        
        return [(x, y) for (distance, (x,y)) in minHeap]