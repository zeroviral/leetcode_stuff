class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Put everything from nums into a dictionary, with mapping as: <number : count>
        2. Put the counts into a heap.
            2.1. While the len(heap) > k, we will heappop() our heap, which removes smallest element.
        3. Return the heap.
        '''
        
        heap = [(count, element) for element, count in Counter(nums).items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [element for (count, element) in heap]