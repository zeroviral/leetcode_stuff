class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        lookup = collections.defaultdict(int)
        
        uniques = 0
        total = 0
        l = 0
        
        for r in range(len(s)):
            lookup[s[r]] += 1
            
            if lookup[s[r]] == 1:
                uniques += 1
            
            while r - l + 1 > 3:
                lookup[s[l]] -= 1
                
                if lookup[s[l]] < 1:
                    uniques -= 1
                l += 1
            
            if uniques == 3:
                total += 1
        return total
                