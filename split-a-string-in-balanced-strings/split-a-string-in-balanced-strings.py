class Solution:
    def balancedStringSplit(self, s: str) -> int:
        split = rCount = lCount = 0
        
        for c in s:
            if c == "R":
                rCount += 1
            else:
                lCount += 1
            if rCount == lCount:
                split += 1
        return split