from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        lookup = set()
        
        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l += 1
            lookup.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength    