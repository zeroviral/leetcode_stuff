class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        
        if len(nums) == 0:
            return
        
        while r < len(nums):
            if nums[l] != 0:
                if nums[r] == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    r += 1
                    l += 1
                else:
                    r += 1
            else:
                l += 1
                r = max(l, r)
        
        r, l = len(nums) - 1, len(nums) - 2
        
        while l >= 0:
            if nums[r] != 2:
                if nums[l] == 2:
                    nums[l], nums[r] = nums[r], nums[l]
                    l -= 1
                    r -= 1
                else:
                    l -= 1
            else:
                r -= 1
                l = min(l, r)
            