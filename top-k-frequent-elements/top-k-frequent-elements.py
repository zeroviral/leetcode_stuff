class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = Counter(nums)
        
        for key in counts.keys():
            if len(heap) == k:
                heapq.heappushpop(heap, (counts[key], key))
            else:
                heapq.heappush(heap, (counts[key], key))
        
        return [num for (_, num) in heap]