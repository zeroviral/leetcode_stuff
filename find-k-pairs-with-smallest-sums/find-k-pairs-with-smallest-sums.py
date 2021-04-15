class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                currSum = nums1[i] + nums2[j]
                
                if len(minHeap) == k:
                    heapq.heappushpop(minHeap, (-currSum, ([nums1[i], nums2[j]])))
                else:
                    heapq.heappush(minHeap, (-currSum, ([nums1[i], nums2[j]])))
        return [[num1, num2] for (currSum, (num1, num2)) in minHeap]
                    