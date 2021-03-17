class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxVal = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            maxVal = max(nums[i], maxVal)
        return maxVal