class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] > nums[i - 1]:
                currSum += nums[i]
                total = max(total, currSum)
            else:
                currSum = nums[i]
        
        return total
                
        
        