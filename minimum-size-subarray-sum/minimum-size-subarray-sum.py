class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = float('inf')
        currSize = 0
        
        for r in range(len(nums)):
            currSize += nums[r]
        
            while currSize >= target:
                minLength = min(minLength, r - l + 1)
                currSize -= nums[l]
                l += 1
        return minLength if minLength != float('inf') else 0
                