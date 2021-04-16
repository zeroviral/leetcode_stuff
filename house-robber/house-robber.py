class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for element in nums:
            last, now = now, max(now, last + element)
        return now