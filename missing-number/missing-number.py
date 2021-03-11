class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        return sum([num for num in range(len(nums) + 1)]) - sum(nums)