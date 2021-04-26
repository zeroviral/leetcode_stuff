class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        def dfs(index, combo):
            if index == len(nums):
                ans.append(combo.copy())
                return
        
            combo.append(nums[index])
            dfs(index + 1, combo)
            combo.pop()
            dfs(index + 1, combo)
                
        
        ans = []
        dfs(0, [])
        return ans