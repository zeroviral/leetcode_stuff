class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [num for num in nums]
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]