class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = float('inf')
        currSize = 0
        
        r = 0
        
        for i in range(len(nums)):
            currSize += nums[i]
        
            while currSize >= target:
                minLength = min(i - l + 1, minLength)
                currSize -= nums[l]
                l += 1
        return minLength if minLength != float('inf') else 0
                