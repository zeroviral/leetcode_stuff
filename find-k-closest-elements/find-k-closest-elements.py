class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap, ans = [],[]
        
        for element in arr:
            heap.append((abs(x - element), element))
        
        heapq.heapify(heap)
        
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return sorted(ans)