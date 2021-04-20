class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        l = 0
        r = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                element = nums[r]
                r -= 1
            else:
                element = nums[l]
                l += 1
            ans[i] = element ** 2
        return ans