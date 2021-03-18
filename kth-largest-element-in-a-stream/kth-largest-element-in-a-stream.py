import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myList = nums
        self.k = k
        heapq.heapify(self.myList)
        while len(self.myList) > k:
            heapq.heappop(self.myList)

    def add(self, val: int) -> int:
        if len(self.myList) < self.k:
            heapq.heappush(self.myList, val)
        elif val > self.myList[0]:
            heapq.heapreplace(self.myList, val)
        return self.myList[0]
     


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)