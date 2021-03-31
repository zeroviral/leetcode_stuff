from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        lookup = defaultdict(int)
        ans = 0
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            
            while len(lookup) >= 3:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    del lookup[s[l]]
                l += 1
            ans += l
        
        return ans