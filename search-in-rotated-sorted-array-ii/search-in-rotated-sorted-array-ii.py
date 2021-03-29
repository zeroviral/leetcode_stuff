class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for r in range(len(nums)):
            if nums[r] == target:
                return True
        return False