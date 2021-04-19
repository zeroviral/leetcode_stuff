class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[index] for index, c in enumerate(combo) if c == '1'] for combo in ["{0:b}".format(i).zfill(len(nums)) for i in range(2 ** len(nums))]]
        