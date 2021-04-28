class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def dfs(start, combo):
            ans.append(combo.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                combo.append(nums[i])
                dfs(i + 1, combo)
                combo.pop()
        
        dfs(0, [])
        return ans