class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        temp = 0
        
        for i in range(len(nums)):
            temp += nums[i]
            nums[i] = temp
        
        return nums