class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        ans = []
        
        for c in s:
            if c == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        return ans + [l]