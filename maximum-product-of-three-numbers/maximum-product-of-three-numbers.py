class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        top3 = 1
        top3 = nums[-3] * nums[-2] * nums[-1]
        
        bottom3 = nums[-1] * nums[0] * nums[1]
        
        maxVal = max(bottom3, top3)
        return maxVal