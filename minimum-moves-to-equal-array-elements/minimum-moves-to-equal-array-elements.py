class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] - nums[0] for i in range(len(nums) - 1, 0, -1)])