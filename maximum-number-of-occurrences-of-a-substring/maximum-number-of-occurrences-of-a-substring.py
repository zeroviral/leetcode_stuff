class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # If it meets all conditions, add one to the value of that substring in dictionary
        # keep iterating and 
        l = 0
        lookup = collections.defaultdict(int)
        letters = collections.defaultdict(int)
        count = 0
        maxCount = 0
        
        for r in range(len(s)):
            if letters[s[r]] < 1:
                count += 1
            letters[s[r]] += 1
            
            
            while r - l + 1 > minSize:
                letters[s[l]] -= 1
                if letters[s[l]] < 1:
                    count -= 1
                l += 1

            if minSize <= (r - l + 1) <= maxSize and count <= maxLetters:
                lookup[s[l:r + 1]] += 1
                maxCount = max(maxCount, lookup[s[l:r + 1]])
        return maxCount