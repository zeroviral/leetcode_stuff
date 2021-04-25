class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total = 0
        
        def dfs(index, currSum):
            if index == len(nums):
                if currSum == target:
                    self.total += 1
                return
            dfs(index + 1, currSum + nums[index])
            dfs(index + 1, currSum - nums[index])
        
        dfs(0, 0)
        return self.total