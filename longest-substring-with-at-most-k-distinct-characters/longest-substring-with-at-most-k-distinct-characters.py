from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lookup = defaultdict(int)
        l = 0
        maxLength = 0
        count = 0
        
        for r in range(len(s)):
            if s[r] not in lookup or lookup[s[r]] == 0:
                count += 1
            lookup[s[r]] += 1
            
            while l <= r and count > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    count -= 1
                l += 1
            
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength