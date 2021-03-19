class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        lookup = Counter(s1)
        count = 0
        
        for r in range(len(s2)):
            if s2[r] in lookup:
                if lookup[s2[r]] > 0:
                    count += 1
                lookup[s2[r]] -= 1
            while l <= r and r - l + 1 > len(s1):
                if s2[l] in lookup:
                    lookup[s2[l]] += 1
                    if lookup[s2[l]] > 0:
                        count -= 1
                l += 1
            if count == len(s1):
                return True
        return False