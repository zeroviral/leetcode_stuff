class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if arr[0] >= x:
            return arr[:k]
        
        if arr[-1] <= x:
            return arr[-k:]
        
        l = 0
        r = len(arr) - k
        
        while l < r:
            mid = (l + r) // 2
            
            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                l = mid + 1
            
            else:
                r = mid
        
        return arr[l : l + k]