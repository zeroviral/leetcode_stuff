class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        count = 0
        maxLength = 0
        for r in range(len(A)):
            
            if A[r] == 0:
                count += 1
            
            while l <= r and count > K:
                if A[l] == 0:
                    count -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength
                