class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = float('inf')
        total = 0
        
        for r in range(len(nums)):
            
            total += nums[r]
            
            while l <= r and total >= target:
                minLength = min(minLength, r - l + 1)
                total -= nums[l]
                l += 1
        return minLength if minLength != float('inf') else 0