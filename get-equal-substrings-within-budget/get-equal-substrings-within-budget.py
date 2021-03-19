class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        maxLength = 0
        cost = 0
        
        for r in range(len(s)):
            if s[r] != t[r]:
                cost += abs(ord(s[r]) - ord(t[r]))
                
            while l <= r and cost > maxCost:
                if s[l] != t[l]:
                    cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength