class Solution(object):
    def kClosest(self, points, K):
        maxHeap = []
        
        for x, y in points:
            dist = -(x*x + y*y)
            if len(maxHeap) == K:
                heapq.heappushpop(maxHeap, (dist, (x, y)))
            else:
                heapq.heappush(maxHeap, (dist, (x, y)))
        return [(x, y) for (dist, (x,y)) in maxHeap]
