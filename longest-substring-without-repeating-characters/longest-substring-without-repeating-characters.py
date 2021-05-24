class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        lookup = collections.defaultdict(int)
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            
            while l <= r and lookup[s[r]] > 1:
                lookup[s[l]] -= 1
                l += 1
                
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength