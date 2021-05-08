class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        nums = sorted(heights)
        
        for i, element in enumerate(nums):
            if heights[i] != nums[i]:
                count += 1
        return count