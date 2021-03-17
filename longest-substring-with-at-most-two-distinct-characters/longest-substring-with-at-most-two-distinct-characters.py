from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        types = 0
        lookup = defaultdict(int)
        maxLength = 0
        
        for r in range(len(s)):
            if s[r] not in lookup or lookup[s[r]] == 0:
                types += 1
            lookup[s[r]] += 1
            
            while l <= r and types > 2:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    types -= 1
                l += 1
            if types <= 2:
                maxLength = max(maxLength, len(s[l:r + 1]))
        return maxLength