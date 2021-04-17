class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        total = [(total := total * val) for val in nums]
        if total[-1] == 0: return 0
        elif total[-1] > 0: return 1
        else: return -1
        