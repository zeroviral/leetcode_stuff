class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        l = 0
        count = 0
        ans = 0
        currSum = 0
        
        for r in range(len(A)):
            
            count += A[r]
            
            if A[r] == 1:
                currSum = 0
            
            while l <= r and count >= S:
                if count == S:
                    currSum += 1
                
                count -= A[l]
                l += 1
            ans += currSum
        return ans