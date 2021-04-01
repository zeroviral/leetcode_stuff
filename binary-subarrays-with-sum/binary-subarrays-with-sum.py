class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        l = 0
        count = 0
        ans = 0
        currSum = 0
        
        for r in range(len(A)):
            
            currSum += A[r]
            
            if A[r] == 1:
                count = 0
            
            while l <= r and currSum >= S:
                if currSum == S:
                    count += 1
                
                currSum -= A[l]
                l += 1
            ans += count
        return ans