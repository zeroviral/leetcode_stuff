class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(x - element), element) for element in arr]
        heapq.heapify(heap)
        
        return sorted([heapq.heappop(heap)[1] for i in range(k)])
        