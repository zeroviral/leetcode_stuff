from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:    
        return next(key for key, value in Counter(nums).items() if value > 1)

        