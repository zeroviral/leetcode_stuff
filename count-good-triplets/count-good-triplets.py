class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        count = 0
        
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range(j, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        if i < j and j < k:
                            count += 1
                        
        return count