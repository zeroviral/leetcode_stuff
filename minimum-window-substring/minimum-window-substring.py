class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        count = 0
        minLength = float('inf')
        lookup = Counter(t)
        result = ""
        
        for r in range(len(s)):
            if s[r] in lookup:
                if lookup[s[r]] > 0:
                    count += 1
                lookup[s[r]] -= 1
                
            
            while l <= r and count == len(t):
                if r - l + 1 < minLength:
                    result = s[l:r+1]
                    minLength = r - l + 1
                if s[l] in lookup:
                    lookup[s[l]] += 1
                    if lookup[s[l]] > 0:
                        count -= 1
                l += 1
        return result
        