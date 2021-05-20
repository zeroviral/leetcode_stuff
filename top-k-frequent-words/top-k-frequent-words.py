class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqOfWords = Counter(words)
        
        heap = []
        
        for key, value in freqOfWords.items():
            heapq.heappush(heap, (-value, key))
        
        ans = []
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans