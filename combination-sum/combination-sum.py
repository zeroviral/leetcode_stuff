class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(leftoverDiff, combos, start):
            if leftoverDiff == 0:
                ans.append(combos.copy())
                return
            if leftoverDiff < 0:
                return # Exceeds scope of the allowed values
            
            for i in range(start, len(candidates)):
                combos.append(candidates[i])
                dfs(leftoverDiff - candidates[i], combos, i)
                combos.pop()
        
        dfs(target, [], 0)
        return ans