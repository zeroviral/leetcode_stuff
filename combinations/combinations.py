class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(start, combos):
            if len(combos) == k:
                ans.append(combos.copy())
                return
            for i in range(start, n + 1):
                combos.append(i)    
                dfs(i + 1, combos)
                combos.pop()
        dfs(1, [])
        return ans