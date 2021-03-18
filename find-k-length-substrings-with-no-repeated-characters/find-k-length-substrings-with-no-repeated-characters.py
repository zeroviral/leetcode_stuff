from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l = 0
        seen = defaultdict(int)
        count = 0
        total = 0
        for r in range(len(S)):
            
            if S[r] not in seen or seen[S[r]] == 0:
                count += 1
            seen[S[r]] += 1
            
            while r - l >= K:
                seen[S[l]] -= 1
                if seen[S[l]] == 0:
                    count -= 1
                l += 1
            
            if count == K:
                total += 1
            
        return total