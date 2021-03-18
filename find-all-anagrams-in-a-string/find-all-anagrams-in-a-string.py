class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        lookup = Counter(p)
        count = 0
        ans = []
        
        for r in range(len(s)):
            
            if s[r] in lookup:
                if lookup[s[r]] > 0:
                    count += 1
                lookup[s[r]] -= 1
            
            while r - l + 1 > len(p):
                if s[l] in lookup:
                    lookup[s[l]] += 1
                    if lookup[s[l]] > 0:
                        count -= 1
                l += 1
            
            if count == len(p):
                ans.append(l)
        
        return ans