class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        last = 0
        for i in range(len(nums) - k + 1): 
            if nums[i] > nums[last]: last = i
        return nums[last:last + k]