class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(start):
            if start == len(nums):
                ans.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)
        return ans