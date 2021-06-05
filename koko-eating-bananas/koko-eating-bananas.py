class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def possible(k):    
            return sum((p - 1) // k + 1 for p in piles) <= h
        
        while l < r:
            mid = (l + r) // 2
            if not possible(mid):
                l = mid + 1
            else:
                r = mid
        
        return l