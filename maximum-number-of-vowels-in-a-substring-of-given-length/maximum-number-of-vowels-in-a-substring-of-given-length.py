class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lookup = {
            "a": 1,
            "e": 1,
            "i": 1,
            "o": 1,
            "u": 1
        }
        
        l = 0
        count = 0
        maxLength = 0
        
        for r in range(len(s)):
            
            if s[r] in lookup:
                count += 1
            
            if l <= r and len(s[l:r]) == k:
                if s[l] in lookup:
                    count -= 1
                l += 1
            maxLength = max(maxLength, count)
        return maxLength
                