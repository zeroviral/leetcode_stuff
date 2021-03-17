from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:  
        l = 0
        maxLength = 0
        types = 0
        seen = defaultdict(int)
        
        for r in range(len(s)):
            if s[r] not in seen or seen[s[r]] == 0:
                types += 1
            seen[s[r]] += 1
            
            while l <= r and types > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    types -= 1
                l += 1
            maxLength = max(maxLength, len(s[l:r + 1]))
        return maxLength
                