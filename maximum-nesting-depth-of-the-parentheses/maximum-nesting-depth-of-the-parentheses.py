class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        maxVal = 0
        
        for c in s:
            if c == "(":
                ans += 1
                maxVal = max(ans, maxVal)
            elif c == ")":
                ans -= 1
        return maxVal