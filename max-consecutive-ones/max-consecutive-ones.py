class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxOnes = max(maxOnes, count)
            else:
                count = 0
        
        return maxOnes